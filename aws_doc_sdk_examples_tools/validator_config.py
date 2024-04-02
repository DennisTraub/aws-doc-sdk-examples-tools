# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from typing import Set
from urllib.request import urlopen
import json

# Only files with these extensions are scanned.
EXT_LOOKUP = {
    ".abap": "SAP ABAP",
    ".c": "C",
    ".cmd": "AWS-CLI",
    ".cpp": "C++",
    ".cs": "C#",
    ".css": "CSS",
    ".go": "Go",
    ".html": "JavaScript",
    ".java": "Java",
    ".js": "JavaScript",
    ".json": "JSON",
    ".jsx": "JavaScript",
    ".kt": "Kotlin",
    ".md": "Markdown",
    ".mjs": "JavaScript",
    ".mts": "TypeScript",
    ".php": "PHP",
    ".py": "Python",
    ".rb": "Ruby",
    ".rs": "Rust",
    ".sh": "AWS-CLI",
    ".swift": "Swift",
    ".toml": "Toml",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".txt": "CMake",
    ".yaml": "YAML",
    ".yml": "YAML",
}


def skip(path: Path) -> bool:
    return path.suffix.lower() not in EXT_LOOKUP or path.name in IGNORE_FILES


# If you get a lot of false-flagged 40-character errors
# in specific folders or files, you can omit them from
# these scans by adding them to the following lists.
# However, because this script is mostly run as a GitHub
# action in a clean environment (aside from testing),
# exhaustive ignore lists shouldn"t be necessary.

# Files to skip.
IGNORE_FILES = {
    ".moviedata.json",
    ".travis.yml",
    "AssemblyInfo.cs",
    "moviedata.json",
    "movies.json",
    "movies_5.json",
    "package-lock.json",
}

IGNORE_SPDX_SUFFIXES = {
    ".css",
    ".csv",
    ".html",
    ".json",
    ".md",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}

SPDX_LEADER = r"^(#|//|\") "
SPDX_COPYRIGHT = r"Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved."
SPDX_LICENSE = r"SPDX-License-Identifier: (Apache-2.0|MIT-0)"

GOOD_WORDS = {
    "crash",
    "dp",
    "dummy",
    "massa",
    "jerry",
    "throat",
}

words: Set[str] = set()
try:
    DATA = urlopen(
        "https://raw.githubusercontent.com/zacanger/profane-words/5ad6c62fa5228293bc610602eae475d50036dac2/words.json"
    )
    words = set(json.load(DATA)).difference(GOOD_WORDS)
except:  # noqa: E722
    pass

WORDS = words

# List of words that should never be in code examples.
DENY_LIST = {"alpha-docs-aws.amazon.com", "integ-docs-aws.amazon.com"}.union(WORDS)

# Allowlist of 20- or 40-character strings to allow.
ALLOW_LIST = {
    # Well-known user credentials for testing
    "AIDA123456789EXAMPLE",
    "AIDA987654321EXAMPLE",
    "AROA123456789EXAMPLE",
    "AROA987654321EXAMPLE",
    "ASIAIOSFODNN7EXAMPLE",
    "ASIAI44QH8DHBEXAMPLE",
    "AKIAIOSFODNN7EXAMPLE",
    "AKIAI44QH8DHBEXAMPLE",
    "APKAEIBAERJR2EXAMPLE",
    "APKAEIVFHP46CEXAMPLE",
    "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY",
    # Commit SHAs
    "31c3650d70c243ca7141bb08705102cad89bd0e8",  # Fist commit of this repo
    # Safe look-alikes, mostly tokens and paths that happen to be 40 characters.
    "/AmazonEventBridgeServiceIntegrationTest",
    "/ListOrganizationalUnitsForParentExample",
    "AWSEC2/latest/APIReference/OperationList",
    "AWSManagedDomainsBotnetCommandandControl",
    "AllocatedProvisionedConcurrentExecutions",
    "AppStreamUsageReportsCFNGlueAthenaAccess",
    "AssociateSigninDelegateGroupsWithAccount",
    "AvailableProvisionedConcurrentExecutions",
    "BatchAssociateClientDeviceWithCoreDevice",
    "CancelExportTaskExample/CancelExportTask",
    "CertificateAuthorityExpiryInMilliseconds",
    "CertificateTransparencyLoggingPreference",
    "ChangeMessageVisibilityBatchRequestEntry",
    "CreateCollectionExample/CreateCollection",
    "CreateExportTaskExample/CreateExportTask",
    "DeleteCollectionExample/DeleteCollection",
    "DeleteNetworkInsightsAccessScopeAnalysis",
    "DeleteVpcEndpointConnectionNotifications",
    "DescribeAggregateComplianceByConfigRules",
    "DescribeDbClusterParameterGroupsResponse",
    "DescribeDirectConnectGatewayAssociations",
    "DescribeEffectivePatchesForPatchBaseline",
    "DescribeInstancePatchStatesForPatchGroup",
    "DescribeOrderableDBInstanceOptionsOutput",
    "DescribeReplicationTaskAssessmentResults",
    "DescribeTransitGatewayPeeringAttachments",
    "DescribeVpcEndpointServiceConfigurations",
    "DisassociateAwsAccountFromPartnerAccount",
    "DynamodbRubyExampleCreateUsersTableStack",
    "GetBucketIntelligentTieringConfiguration",
    "GetIdentityVerificationAttributesRequest",
    "GetInstanceTypesFromInstanceRequirements",
    "InstanceAssociationStatusAggregatedCount",
    "InstancesWithCriticalNonCompliantPatches",
    "InstancesWithSecurityNonCompliantPatches",
    "KMSWithContextEncryptionMaterialsExample",
    "KinesisStreamSourceConfiguration=kinesis",
    "ListOrganizationalUnitsForParentResponse",
    "ListTagsExample/ListTagsExample/ListTags",
    "ListTagsForVaultExample/ListTagsForVault",
    "ListVoiceConnectorTerminationCredentials",
    "ModifyReplicationGroupShardConfiguration",
    "ModifyTrafficMirrorFilterNetworkServices",
    "PutBucketIntelligentTieringConfiguration",
    "RequestedProvisionedConcurrentExecutions",
    "SynthesizeSpeechExample/SynthesizeSpeech",
    "TargetTrackingScalingPolicyConfiguration",
    "TerminateInstanceInAutoScalingGroupAsync",
    "UnsuccessfulInstanceCreditSpecifications",
    "UpdateCustomRoutingAcceleratorAttributes",
    "VectorEnrichmentJobDataSourceConfigInput",
    "amazondynamodb/latest/developerguide/DAX",
    "apigateway/latest/developerguide/welcome",
    "aws/acm/model/DescribeCertificateRequest",
    "aws/cloudtrail/model/LookupEventsRequest",
    "aws/codebuild/model/BatchGetBuildsResult",
    "aws/codecommit/model/DeleteBranchRequest",
    "aws/codecommit/model/ListBranchesRequest",
    "aws/dynamodb/model/BatchWriteItemRequest",
    "aws/dynamodb/model/ProvisionedThroughput",
    "aws/ec2/model/CreateSecurityGroupRequest",
    "aws/ec2/model/DeleteSecurityGroupRequest",
    "aws/ec2/model/UnmonitorInstancesResponse",
    "aws/email/model/CreateReceiptRuleRequest",
    "aws/email/model/DeleteReceiptRuleRequest",
    "aws/email/model/ListReceiptFiltersResult",
    "aws/email/model/SendTemplatedEmailResult",
    "aws/guardduty/model/ListDetectorsRequest",
    "aws/iam/model/GetAccessKeyLastUsedResult",
    "aws/iam/model/GetServerCertificateResult",
    "aws/kinesis/model/GetShardIteratorResult",
    "aws/kinesis/model/PutRecordsRequestEntry",
    "aws/kms/model/ScheduleKeyDeletionRequest",
    "aws/monitoring/model/DeleteAlarmsRequest",
    "aws/neptune/model/CreateDBClusterRequest",
    "aws/neptune/model/DeleteDBClusterRequest",
    "aws/neptune/model/ModifyDBClusterRequest",
    "aws/rds/model/DescribeDBInstancesRequest",
    "aws/rds/model/DescribeDBSnapshotsRequest",
    "cloudsearch/latest/developerguide/search",
    "cloudwatch/commands/PutMetricDataCommand",
    "code/codepipeline/MyCodePipelineFunction",
    "codeartifact/latest/APIReference/Welcome",
    "codepipeline/latest/APIReference/Welcome",
    "com/AWSEC2/latest/UserGuide/EBSSnapshots",
    "com/AWSEC2/latest/UserGuide/instancedata",
    "com/AWSJavaScriptSDK/v3/latest/client/s3",
    "com/AmazonCloudWatch/latest/logs/Working",
    "com/AmazonECS/latest/developerguide/task",
    "com/AmazonRDS/latest/AuroraUserGuide/rds",
    "com/AmazonS3/latest/API/RESTBucketPUTacl",
    "com/AmazonS3/latest/userguide/ServerLogs",
    "com/AmazonServiceRoleForLexBots/1a2b3c4d",
    "com/Route53/latest/DeveloperGuide/domain",
    "com/amazondynamodb/latest/developerguide",
    "com/apigateway/latest/developerguide/api",
    "com/apigateway/latest/developerguide/how",
    "com/apigateway/latest/developerguide/set",
    "com/appconfig/latest/userguide/appconfig",
    "com/autoscaling/ec2/APIReference/Welcome",
    "com/awssupport/latest/APIReference/index",
    "com/directconnect/latest/UserGuide/multi",
    "com/documentdb/latest/developerguide/API",
    "com/firehose/latest/APIReference/Welcome",
    "com/greengrass/latest/developerguide/lra",
    "com/greengrass/latest/developerguide/sns",
    "com/healthimaging/latest/devguide/create",
    "com/healthimaging/latest/devguide/delete",
    "com/healthimaging/latest/devguide/search",
    "com/healthimaging/latest/devguide/update",
    "com/inspector/latest/userguide/inspector",
    "com/iot/latest/developerguide/mitigation",
    "com/iotanalytics/latest/APIReference/API",
    "com/kms/latest/developerguide/disconnect",
    "com/kotlin/api/latest/mediaconvert/index",
    "com/mediatailor/latest/ug/configurations",
    "com/pinpoint/latest/apireference/welcome",
    "com/redshift/latest/APIReference/Welcome",
    "com/rekognition/latest/dg/considerations",
    "com/samples/JobStatusNotificationsSample",
    "com/secretsmanager/latest/userguide/auth",
    "com/securityhub/latest/userguide/finding",
    "com/servicecatalog/latest/arguide/access",
    "com/servicecatalog/latest/arguide/create",
    "com/servicecatalog/latest/arguide/delete",
    "com/servicecatalog/latest/arguide/manage",
    "com/transcribe/latest/APIReference/index",
    "com/v1/documentation/api/latest/guide/s3",
    "com/workdocs/latest/APIReference/Welcome",
    "com/workspaces/latest/adminguide/migrate",
    "com/workspaces/latest/adminguide/rebuild",
    "com/workspaces/latest/adminguide/restore",
    "com/workspaces/latest/adminguide/running",
    "cryptography/latest/APIReference/Welcome",
    "datapipeline/latest/APIReference/Welcome",
    "devicefarm/latest/developerguide/welcome",
    "directConnectGatewayAssociationProposals",
    "examples/blob/main/applications/feedback",
    "exclusiveResourceSecurityGroupManagement",
    "generate_presigned_url_and_upload_object",
    "iam/commands/GetAccessKeyLastUsedCommand",
    "iam/commands/GetServerCertificateCommand",
    "imagebuilder/latest/APIReference/Welcome",
    "imaging/model/GetImageSetMetadataRequest",
    "imaging/model/StartDICOMImportJobRequest",
    "iotanalytics/latest/APIReference/Welcome",
    "mediaconnect/latest/APIReference/Welcome",
    "nFindProductsWithNegativePriceWithConfig",
    "preview/examples/cognitoidentityprovider",
    "preview/examples/lambda/src/bin/scenario",
    "respondToDevicePasswordVerifierChallenge",
    "role/AmazonBedrockExecutionRoleForAgents",
    "role/AmazonSageMakerGeospatialFullAccess",
    "s3_client_side_encryption_sym_master_key",
    "serial/CORE_THING_NAME/write/dev/serial1",
    "service/FeedbackSentimentAnalyzer/README",
    "ses/commands/CreateReceiptRuleSetCommand",
    "ses/commands/DeleteReceiptRuleSetCommand",
    "ses/commands/VerifyDomainIdentityCommand",
    "src/main/java/com/aws/jdbc/RetrieveItems",
    "src/main/java/com/etl/example/Population",
    "src/main/java/com/example/RDSGetStudents",
    "src/main/java/com/example/commit/PutFile",
    "src/main/java/com/example/dynamodb/Query",
    "src/main/java/com/example/glue/GetJobRun",
    "src/main/java/com/example/glue/HelloGlue",
    "src/main/java/com/example/iam/CreateRole",
    "src/main/java/com/example/iam/CreateUser",
    "src/main/java/com/example/iam/DeleteUser",
    "src/main/java/com/example/iam/UpdateUser",
    "src/main/java/com/example/kms/ListGrants",
    "src/main/java/com/example/photo/WorkItem",
    "src/main/java/com/example/ppe/PPEHandler",
    "src/main/java/com/example/s3/ListBuckets",
    "src/main/java/com/example/s3/ListObjects",
    "src/main/java/com/example/s3/S3BucketOps",
    "src/main/java/com/example/sns/ListOptOut",
    "src/main/java/com/example/sns/ListTopics",
    "src/main/java/com/example/sqs/SQSExample",
    "src/main/java/com/example/ssm/GetOpsItem",
    "src/main/java/com/example/sts/AssumeRole",
    "src/main/java/com/example/tags/S3Service",
    "src/main/kotlin/com/kotlin/iam/GetPolicy",
    "src/main/kotlin/com/kotlin/iam/ListUsers",
    "src/main/kotlin/com/kotlin/s3/CopyObject",
    "src/test/java/example/firehose/PutRecord",
    "targetTrackingScalingPolicyConfiguration",
    "upload_files_using_managed_file_uploader",
    "videoMetaData=celebrityRecognitionResult",
    "s3/src/main/java/com/example/s3/ParseUri",
    "https://docs.aws.amazon.com/ivs/latest/userguide//private-channels.html",
}


# Sample files.
EXPECTED_SAMPLE_FILES = {
    "README.md",
    "chat_sfn_state_machine.json",
    "market_2.jpg",
    "movies.json",
    "sample_saml_metadata.xml",
    "speech_sample.mp3",
    "spheres_2.jpg",
}

# Media file types.
MEDIA_FILE_TYPES = {"mp3", "wav", "jpg", "jpeg", "png"}
