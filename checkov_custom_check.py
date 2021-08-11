# Run using:
#   checkov -d tfdir --external-checks-dir /path/to/custom/checks -c CUSTOM_S3_ENCRYPTED'
# /path/to/custom/checks/__init__.py must contain the code described in https://www.checkov.io/2.Concepts/Custom%20Policies.html
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck



class UnencryptedS3Bucket(BaseResourceCheck):
    def __init__(self):
        name = "Ensure S3 bucket is encrypted at rest"
        id = "CUSTOM_S3_ENCRYPTED"
        supported_resources = ['aws_s3_bucket']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
    def scan_resource_conf(self, conf):
        if 'server_side_encryption_configuration' not in conf.keys():
            return CheckResult.FAILED
        
        return CheckResult.PASSED
scanner = UnencryptedS3Bucket()