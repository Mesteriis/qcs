import contextlib
import subprocess
from datetime import datetime
from typing import List, Optional

from django.utils.timezone import utc

from files.models import CodeFile
from reports.constants import ReportStatus
from reports.models import Report


class CQService:
    @classmethod
    def __check_file(cls, file_path) -> str:
        bashCommand = f"flake8 {file_path}"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, _ = process.communicate()
        return output.decode("utf-8")

    @classmethod
    def check_from_model(cls, file: CodeFile):
        return cls.__build_report(file, cls.__check_file(file.file.path))

    @classmethod
    def __build_report(cls, file: CodeFile, report: Optional[str] = None) -> Report:
        with contextlib.suppress(Exception):
            file.report.delete()
        data = {
            "user": file.user,
            "file": file,
            "created": datetime.now(tz=utc),
            "status": ReportStatus.FAIL if report else ReportStatus.SUCCESS,
            "result": None,
        }
        if report:
            report = report.replace(f"{file.file.path}:", "str:").split("\n")
            fail_str_count = cls.__extract_fail_str_indices(report)
            fail_str_index = list(map(lambda x: x - 1, fail_str_count))  # noqa C417
            lines = cls.__read_file(file.file.path)
            fail_lines = [
                line.strip() for inx, line in enumerate(lines) if inx in fail_str_index
            ]
            data["result"] = [
                {
                    "line": line,
                    "error": cls.__handler_error_str(error),
                    "number": number_str,
                }
                for line, error, number_str in zip(
                    fail_lines,
                    report,
                    fail_str_count,
                )
            ]
        return Report.objects.create(**data)

    @staticmethod
    def __read_file(file_path: str) -> List[str]:
        with open(file_path) as f:
            return f.readlines()

    @staticmethod
    def __extract_fail_str_indices(text: List[str]) -> list[int]:
        return [int(el[4 : el[4:].index(":") + 4]) for el in text if el]  # noqa E203

    @staticmethod
    def __handler_error_str(text: str) -> dict[str, str]:
        string = text.split(": ")[1][:]
        code = string[: string.index(" ")]
        type_ = code[0]
        return {
            "code": code,
            "string": string.replace(code, ""),
            "type": type_,
        }
