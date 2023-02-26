from logging import Filter


class SkipStaticFilter(Filter):
    """Logging filter to skip logging of staticfiles to terminal"""

    def filter(self, record):
        if (
            "GET /static/" in record.getMessage()
            or "GET /admin/" in record.getMessage()
        ):
            return None
        return record
