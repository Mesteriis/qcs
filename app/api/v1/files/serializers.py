from rest_framework import serializers

from files.models import CodeFile


class CodeFilesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    file_name = serializers.SerializerMethodField("get_file_name", read_only=True)
    pk = serializers.UUIDField(read_only=True)
    status = serializers.CharField(read_only=True)

    @staticmethod
    def get_file_name(obj) -> str:
        return obj.file.name.split("/")[-1]

    class Meta:
        model = CodeFile
        fields = [
            "pk",
            "file",
            "status",
            "user",
            "file_name",
            "created",
        ]
