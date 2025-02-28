# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AccountListPoolNodeCountsOptions
    from ._models_py3 import AccountListSupportedImagesOptions
    from ._models_py3 import AffinityInformation
    from ._models_py3 import ApplicationGetOptions
    from ._models_py3 import ApplicationListOptions
    from ._models_py3 import ApplicationPackageReference
    from ._models_py3 import ApplicationSummary
    from ._models_py3 import AuthenticationTokenSettings
    from ._models_py3 import AutoPoolSpecification
    from ._models_py3 import AutoScaleRun
    from ._models_py3 import AutoScaleRunError
    from ._models_py3 import AutoUserSpecification
    from ._models_py3 import AzureBlobFileSystemConfiguration
    from ._models_py3 import AzureFileShareConfiguration
    from ._models_py3 import BatchError, BatchErrorException
    from ._models_py3 import BatchErrorDetail
    from ._models_py3 import BatchPoolIdentity
    from ._models_py3 import Certificate
    from ._models_py3 import CertificateAddOptions
    from ._models_py3 import CertificateAddParameter
    from ._models_py3 import CertificateCancelDeletionOptions
    from ._models_py3 import CertificateDeleteOptions
    from ._models_py3 import CertificateGetOptions
    from ._models_py3 import CertificateListOptions
    from ._models_py3 import CertificateReference
    from ._models_py3 import CIFSMountConfiguration
    from ._models_py3 import CloudJob
    from ._models_py3 import CloudJobSchedule
    from ._models_py3 import CloudPool
    from ._models_py3 import CloudServiceConfiguration
    from ._models_py3 import CloudTask
    from ._models_py3 import CloudTaskListSubtasksResult
    from ._models_py3 import ComputeNode
    from ._models_py3 import ComputeNodeAddUserOptions
    from ._models_py3 import ComputeNodeDeleteUserOptions
    from ._models_py3 import ComputeNodeDisableSchedulingOptions
    from ._models_py3 import ComputeNodeEnableSchedulingOptions
    from ._models_py3 import ComputeNodeEndpointConfiguration
    from ._models_py3 import ComputeNodeError
    from ._models_py3 import ComputeNodeExtensionGetOptions
    from ._models_py3 import ComputeNodeExtensionListOptions
    from ._models_py3 import ComputeNodeGetOptions
    from ._models_py3 import ComputeNodeGetRemoteDesktopOptions
    from ._models_py3 import ComputeNodeGetRemoteLoginSettingsOptions
    from ._models_py3 import ComputeNodeGetRemoteLoginSettingsResult
    from ._models_py3 import ComputeNodeIdentityReference
    from ._models_py3 import ComputeNodeInformation
    from ._models_py3 import ComputeNodeListOptions
    from ._models_py3 import ComputeNodeRebootOptions
    from ._models_py3 import ComputeNodeReimageOptions
    from ._models_py3 import ComputeNodeUpdateUserOptions
    from ._models_py3 import ComputeNodeUploadBatchServiceLogsOptions
    from ._models_py3 import ComputeNodeUser
    from ._models_py3 import ContainerConfiguration
    from ._models_py3 import ContainerRegistry
    from ._models_py3 import DataDisk
    from ._models_py3 import DeleteCertificateError
    from ._models_py3 import DiffDiskSettings
    from ._models_py3 import DiskEncryptionConfiguration
    from ._models_py3 import EnvironmentSetting
    from ._models_py3 import ErrorMessage
    from ._models_py3 import ExitCodeMapping
    from ._models_py3 import ExitCodeRangeMapping
    from ._models_py3 import ExitConditions
    from ._models_py3 import ExitOptions
    from ._models_py3 import FileDeleteFromComputeNodeOptions
    from ._models_py3 import FileDeleteFromTaskOptions
    from ._models_py3 import FileGetFromComputeNodeOptions
    from ._models_py3 import FileGetFromTaskOptions
    from ._models_py3 import FileGetPropertiesFromComputeNodeOptions
    from ._models_py3 import FileGetPropertiesFromTaskOptions
    from ._models_py3 import FileListFromComputeNodeOptions
    from ._models_py3 import FileListFromTaskOptions
    from ._models_py3 import FileProperties
    from ._models_py3 import HttpHeader
    from ._models_py3 import ImageInformation
    from ._models_py3 import ImageReference
    from ._models_py3 import InboundEndpoint
    from ._models_py3 import InboundNATPool
    from ._models_py3 import InstanceViewStatus
    from ._models_py3 import JobAddOptions
    from ._models_py3 import JobAddParameter
    from ._models_py3 import JobConstraints
    from ._models_py3 import JobDeleteOptions
    from ._models_py3 import JobDisableOptions
    from ._models_py3 import JobDisableParameter
    from ._models_py3 import JobEnableOptions
    from ._models_py3 import JobExecutionInformation
    from ._models_py3 import JobGetAllLifetimeStatisticsOptions
    from ._models_py3 import JobGetOptions
    from ._models_py3 import JobGetTaskCountsOptions
    from ._models_py3 import JobListFromJobScheduleOptions
    from ._models_py3 import JobListOptions
    from ._models_py3 import JobListPreparationAndReleaseTaskStatusOptions
    from ._models_py3 import JobManagerTask
    from ._models_py3 import JobNetworkConfiguration
    from ._models_py3 import JobPatchOptions
    from ._models_py3 import JobPatchParameter
    from ._models_py3 import JobPreparationAndReleaseTaskExecutionInformation
    from ._models_py3 import JobPreparationTask
    from ._models_py3 import JobPreparationTaskExecutionInformation
    from ._models_py3 import JobReleaseTask
    from ._models_py3 import JobReleaseTaskExecutionInformation
    from ._models_py3 import JobScheduleAddOptions
    from ._models_py3 import JobScheduleAddParameter
    from ._models_py3 import JobScheduleDeleteOptions
    from ._models_py3 import JobScheduleDisableOptions
    from ._models_py3 import JobScheduleEnableOptions
    from ._models_py3 import JobScheduleExecutionInformation
    from ._models_py3 import JobScheduleExistsOptions
    from ._models_py3 import JobScheduleGetOptions
    from ._models_py3 import JobScheduleListOptions
    from ._models_py3 import JobSchedulePatchOptions
    from ._models_py3 import JobSchedulePatchParameter
    from ._models_py3 import JobScheduleStatistics
    from ._models_py3 import JobScheduleTerminateOptions
    from ._models_py3 import JobScheduleUpdateOptions
    from ._models_py3 import JobScheduleUpdateParameter
    from ._models_py3 import JobSchedulingError
    from ._models_py3 import JobSpecification
    from ._models_py3 import JobStatistics
    from ._models_py3 import JobTerminateOptions
    from ._models_py3 import JobTerminateParameter
    from ._models_py3 import JobUpdateOptions
    from ._models_py3 import JobUpdateParameter
    from ._models_py3 import LinuxUserConfiguration
    from ._models_py3 import MetadataItem
    from ._models_py3 import MountConfiguration
    from ._models_py3 import MultiInstanceSettings
    from ._models_py3 import NameValuePair
    from ._models_py3 import NetworkConfiguration
    from ._models_py3 import NetworkSecurityGroupRule
    from ._models_py3 import NFSMountConfiguration
    from ._models_py3 import NodeAgentInformation
    from ._models_py3 import NodeCounts
    from ._models_py3 import NodeDisableSchedulingParameter
    from ._models_py3 import NodeFile
    from ._models_py3 import NodePlacementConfiguration
    from ._models_py3 import NodeRebootParameter
    from ._models_py3 import NodeReimageParameter
    from ._models_py3 import NodeRemoveParameter
    from ._models_py3 import NodeUpdateUserParameter
    from ._models_py3 import NodeVMExtension
    from ._models_py3 import OSDisk
    from ._models_py3 import OutputFile
    from ._models_py3 import OutputFileBlobContainerDestination
    from ._models_py3 import OutputFileDestination
    from ._models_py3 import OutputFileUploadOptions
    from ._models_py3 import PoolAddOptions
    from ._models_py3 import PoolAddParameter
    from ._models_py3 import PoolDeleteOptions
    from ._models_py3 import PoolDisableAutoScaleOptions
    from ._models_py3 import PoolEnableAutoScaleOptions
    from ._models_py3 import PoolEnableAutoScaleParameter
    from ._models_py3 import PoolEndpointConfiguration
    from ._models_py3 import PoolEvaluateAutoScaleOptions
    from ._models_py3 import PoolEvaluateAutoScaleParameter
    from ._models_py3 import PoolExistsOptions
    from ._models_py3 import PoolGetAllLifetimeStatisticsOptions
    from ._models_py3 import PoolGetOptions
    from ._models_py3 import PoolInformation
    from ._models_py3 import PoolListOptions
    from ._models_py3 import PoolListUsageMetricsOptions
    from ._models_py3 import PoolNodeCounts
    from ._models_py3 import PoolPatchOptions
    from ._models_py3 import PoolPatchParameter
    from ._models_py3 import PoolRemoveNodesOptions
    from ._models_py3 import PoolResizeOptions
    from ._models_py3 import PoolResizeParameter
    from ._models_py3 import PoolSpecification
    from ._models_py3 import PoolStatistics
    from ._models_py3 import PoolStopResizeOptions
    from ._models_py3 import PoolUpdatePropertiesOptions
    from ._models_py3 import PoolUpdatePropertiesParameter
    from ._models_py3 import PoolUsageMetrics
    from ._models_py3 import PublicIPAddressConfiguration
    from ._models_py3 import RecentJob
    from ._models_py3 import ResizeError
    from ._models_py3 import ResourceFile
    from ._models_py3 import ResourceStatistics
    from ._models_py3 import Schedule
    from ._models_py3 import StartTask
    from ._models_py3 import StartTaskInformation
    from ._models_py3 import SubtaskInformation
    from ._models_py3 import TaskAddCollectionOptions
    from ._models_py3 import TaskAddCollectionParameter
    from ._models_py3 import TaskAddCollectionResult
    from ._models_py3 import TaskAddOptions
    from ._models_py3 import TaskAddParameter
    from ._models_py3 import TaskAddResult
    from ._models_py3 import TaskConstraints
    from ._models_py3 import TaskContainerExecutionInformation
    from ._models_py3 import TaskContainerSettings
    from ._models_py3 import TaskCounts
    from ._models_py3 import TaskCountsResult
    from ._models_py3 import TaskDeleteOptions
    from ._models_py3 import TaskDependencies
    from ._models_py3 import TaskExecutionInformation
    from ._models_py3 import TaskFailureInformation
    from ._models_py3 import TaskGetOptions
    from ._models_py3 import TaskIdRange
    from ._models_py3 import TaskInformation
    from ._models_py3 import TaskListOptions
    from ._models_py3 import TaskListSubtasksOptions
    from ._models_py3 import TaskReactivateOptions
    from ._models_py3 import TaskSchedulingPolicy
    from ._models_py3 import TaskSlotCounts
    from ._models_py3 import TaskStatistics
    from ._models_py3 import TaskTerminateOptions
    from ._models_py3 import TaskUpdateOptions
    from ._models_py3 import TaskUpdateParameter
    from ._models_py3 import UploadBatchServiceLogsConfiguration
    from ._models_py3 import UploadBatchServiceLogsResult
    from ._models_py3 import UsageStatistics
    from ._models_py3 import UserAccount
    from ._models_py3 import UserAssignedIdentity
    from ._models_py3 import UserIdentity
    from ._models_py3 import VirtualMachineConfiguration
    from ._models_py3 import VirtualMachineInfo
    from ._models_py3 import VMExtension
    from ._models_py3 import VMExtensionInstanceView
    from ._models_py3 import WindowsConfiguration
    from ._models_py3 import WindowsUserConfiguration
except (SyntaxError, ImportError):
    from ._models import AccountListPoolNodeCountsOptions
    from ._models import AccountListSupportedImagesOptions
    from ._models import AffinityInformation
    from ._models import ApplicationGetOptions
    from ._models import ApplicationListOptions
    from ._models import ApplicationPackageReference
    from ._models import ApplicationSummary
    from ._models import AuthenticationTokenSettings
    from ._models import AutoPoolSpecification
    from ._models import AutoScaleRun
    from ._models import AutoScaleRunError
    from ._models import AutoUserSpecification
    from ._models import AzureBlobFileSystemConfiguration
    from ._models import AzureFileShareConfiguration
    from ._models import BatchError, BatchErrorException
    from ._models import BatchErrorDetail
    from ._models import BatchPoolIdentity
    from ._models import Certificate
    from ._models import CertificateAddOptions
    from ._models import CertificateAddParameter
    from ._models import CertificateCancelDeletionOptions
    from ._models import CertificateDeleteOptions
    from ._models import CertificateGetOptions
    from ._models import CertificateListOptions
    from ._models import CertificateReference
    from ._models import CIFSMountConfiguration
    from ._models import CloudJob
    from ._models import CloudJobSchedule
    from ._models import CloudPool
    from ._models import CloudServiceConfiguration
    from ._models import CloudTask
    from ._models import CloudTaskListSubtasksResult
    from ._models import ComputeNode
    from ._models import ComputeNodeAddUserOptions
    from ._models import ComputeNodeDeleteUserOptions
    from ._models import ComputeNodeDisableSchedulingOptions
    from ._models import ComputeNodeEnableSchedulingOptions
    from ._models import ComputeNodeEndpointConfiguration
    from ._models import ComputeNodeError
    from ._models import ComputeNodeExtensionGetOptions
    from ._models import ComputeNodeExtensionListOptions
    from ._models import ComputeNodeGetOptions
    from ._models import ComputeNodeGetRemoteDesktopOptions
    from ._models import ComputeNodeGetRemoteLoginSettingsOptions
    from ._models import ComputeNodeGetRemoteLoginSettingsResult
    from ._models import ComputeNodeIdentityReference
    from ._models import ComputeNodeInformation
    from ._models import ComputeNodeListOptions
    from ._models import ComputeNodeRebootOptions
    from ._models import ComputeNodeReimageOptions
    from ._models import ComputeNodeUpdateUserOptions
    from ._models import ComputeNodeUploadBatchServiceLogsOptions
    from ._models import ComputeNodeUser
    from ._models import ContainerConfiguration
    from ._models import ContainerRegistry
    from ._models import DataDisk
    from ._models import DeleteCertificateError
    from ._models import DiffDiskSettings
    from ._models import DiskEncryptionConfiguration
    from ._models import EnvironmentSetting
    from ._models import ErrorMessage
    from ._models import ExitCodeMapping
    from ._models import ExitCodeRangeMapping
    from ._models import ExitConditions
    from ._models import ExitOptions
    from ._models import FileDeleteFromComputeNodeOptions
    from ._models import FileDeleteFromTaskOptions
    from ._models import FileGetFromComputeNodeOptions
    from ._models import FileGetFromTaskOptions
    from ._models import FileGetPropertiesFromComputeNodeOptions
    from ._models import FileGetPropertiesFromTaskOptions
    from ._models import FileListFromComputeNodeOptions
    from ._models import FileListFromTaskOptions
    from ._models import FileProperties
    from ._models import HttpHeader
    from ._models import ImageInformation
    from ._models import ImageReference
    from ._models import InboundEndpoint
    from ._models import InboundNATPool
    from ._models import InstanceViewStatus
    from ._models import JobAddOptions
    from ._models import JobAddParameter
    from ._models import JobConstraints
    from ._models import JobDeleteOptions
    from ._models import JobDisableOptions
    from ._models import JobDisableParameter
    from ._models import JobEnableOptions
    from ._models import JobExecutionInformation
    from ._models import JobGetAllLifetimeStatisticsOptions
    from ._models import JobGetOptions
    from ._models import JobGetTaskCountsOptions
    from ._models import JobListFromJobScheduleOptions
    from ._models import JobListOptions
    from ._models import JobListPreparationAndReleaseTaskStatusOptions
    from ._models import JobManagerTask
    from ._models import JobNetworkConfiguration
    from ._models import JobPatchOptions
    from ._models import JobPatchParameter
    from ._models import JobPreparationAndReleaseTaskExecutionInformation
    from ._models import JobPreparationTask
    from ._models import JobPreparationTaskExecutionInformation
    from ._models import JobReleaseTask
    from ._models import JobReleaseTaskExecutionInformation
    from ._models import JobScheduleAddOptions
    from ._models import JobScheduleAddParameter
    from ._models import JobScheduleDeleteOptions
    from ._models import JobScheduleDisableOptions
    from ._models import JobScheduleEnableOptions
    from ._models import JobScheduleExecutionInformation
    from ._models import JobScheduleExistsOptions
    from ._models import JobScheduleGetOptions
    from ._models import JobScheduleListOptions
    from ._models import JobSchedulePatchOptions
    from ._models import JobSchedulePatchParameter
    from ._models import JobScheduleStatistics
    from ._models import JobScheduleTerminateOptions
    from ._models import JobScheduleUpdateOptions
    from ._models import JobScheduleUpdateParameter
    from ._models import JobSchedulingError
    from ._models import JobSpecification
    from ._models import JobStatistics
    from ._models import JobTerminateOptions
    from ._models import JobTerminateParameter
    from ._models import JobUpdateOptions
    from ._models import JobUpdateParameter
    from ._models import LinuxUserConfiguration
    from ._models import MetadataItem
    from ._models import MountConfiguration
    from ._models import MultiInstanceSettings
    from ._models import NameValuePair
    from ._models import NetworkConfiguration
    from ._models import NetworkSecurityGroupRule
    from ._models import NFSMountConfiguration
    from ._models import NodeAgentInformation
    from ._models import NodeCounts
    from ._models import NodeDisableSchedulingParameter
    from ._models import NodeFile
    from ._models import NodePlacementConfiguration
    from ._models import NodeRebootParameter
    from ._models import NodeReimageParameter
    from ._models import NodeRemoveParameter
    from ._models import NodeUpdateUserParameter
    from ._models import NodeVMExtension
    from ._models import OSDisk
    from ._models import OutputFile
    from ._models import OutputFileBlobContainerDestination
    from ._models import OutputFileDestination
    from ._models import OutputFileUploadOptions
    from ._models import PoolAddOptions
    from ._models import PoolAddParameter
    from ._models import PoolDeleteOptions
    from ._models import PoolDisableAutoScaleOptions
    from ._models import PoolEnableAutoScaleOptions
    from ._models import PoolEnableAutoScaleParameter
    from ._models import PoolEndpointConfiguration
    from ._models import PoolEvaluateAutoScaleOptions
    from ._models import PoolEvaluateAutoScaleParameter
    from ._models import PoolExistsOptions
    from ._models import PoolGetAllLifetimeStatisticsOptions
    from ._models import PoolGetOptions
    from ._models import PoolInformation
    from ._models import PoolListOptions
    from ._models import PoolListUsageMetricsOptions
    from ._models import PoolNodeCounts
    from ._models import PoolPatchOptions
    from ._models import PoolPatchParameter
    from ._models import PoolRemoveNodesOptions
    from ._models import PoolResizeOptions
    from ._models import PoolResizeParameter
    from ._models import PoolSpecification
    from ._models import PoolStatistics
    from ._models import PoolStopResizeOptions
    from ._models import PoolUpdatePropertiesOptions
    from ._models import PoolUpdatePropertiesParameter
    from ._models import PoolUsageMetrics
    from ._models import PublicIPAddressConfiguration
    from ._models import RecentJob
    from ._models import ResizeError
    from ._models import ResourceFile
    from ._models import ResourceStatistics
    from ._models import Schedule
    from ._models import StartTask
    from ._models import StartTaskInformation
    from ._models import SubtaskInformation
    from ._models import TaskAddCollectionOptions
    from ._models import TaskAddCollectionParameter
    from ._models import TaskAddCollectionResult
    from ._models import TaskAddOptions
    from ._models import TaskAddParameter
    from ._models import TaskAddResult
    from ._models import TaskConstraints
    from ._models import TaskContainerExecutionInformation
    from ._models import TaskContainerSettings
    from ._models import TaskCounts
    from ._models import TaskCountsResult
    from ._models import TaskDeleteOptions
    from ._models import TaskDependencies
    from ._models import TaskExecutionInformation
    from ._models import TaskFailureInformation
    from ._models import TaskGetOptions
    from ._models import TaskIdRange
    from ._models import TaskInformation
    from ._models import TaskListOptions
    from ._models import TaskListSubtasksOptions
    from ._models import TaskReactivateOptions
    from ._models import TaskSchedulingPolicy
    from ._models import TaskSlotCounts
    from ._models import TaskStatistics
    from ._models import TaskTerminateOptions
    from ._models import TaskUpdateOptions
    from ._models import TaskUpdateParameter
    from ._models import UploadBatchServiceLogsConfiguration
    from ._models import UploadBatchServiceLogsResult
    from ._models import UsageStatistics
    from ._models import UserAccount
    from ._models import UserAssignedIdentity
    from ._models import UserIdentity
    from ._models import VirtualMachineConfiguration
    from ._models import VirtualMachineInfo
    from ._models import VMExtension
    from ._models import VMExtensionInstanceView
    from ._models import WindowsConfiguration
    from ._models import WindowsUserConfiguration
from ._paged_models import ApplicationSummaryPaged
from ._paged_models import CertificatePaged
from ._paged_models import CloudJobPaged
from ._paged_models import CloudJobSchedulePaged
from ._paged_models import CloudPoolPaged
from ._paged_models import CloudTaskPaged
from ._paged_models import ComputeNodePaged
from ._paged_models import ImageInformationPaged
from ._paged_models import JobPreparationAndReleaseTaskExecutionInformationPaged
from ._paged_models import NodeFilePaged
from ._paged_models import NodeVMExtensionPaged
from ._paged_models import PoolNodeCountsPaged
from ._paged_models import PoolUsageMetricsPaged
from ._batch_service_client_enums import (
    OSType,
    VerificationType,
    AccessScope,
    CertificateState,
    CertificateFormat,
    ContainerWorkingDirectory,
    JobAction,
    DependencyAction,
    AutoUserScope,
    ElevationLevel,
    LoginMode,
    OutputFileUploadCondition,
    ComputeNodeFillType,
    CertificateStoreLocation,
    CertificateVisibility,
    CachingType,
    StorageAccountType,
    DiskEncryptionTarget,
    NodePlacementPolicyType,
    DiffDiskPlacement,
    DynamicVNetAssignmentScope,
    InboundEndpointProtocol,
    NetworkSecurityGroupRuleAccess,
    IPAddressProvisioningType,
    NodeCommunicationMode,
    PoolLifetimeOption,
    OnAllTasksComplete,
    OnTaskFailure,
    JobScheduleState,
    ErrorCategory,
    JobState,
    JobPreparationTaskState,
    TaskExecutionResult,
    JobReleaseTaskState,
    ContainerType,
    StatusLevelTypes,
    PoolState,
    AllocationState,
    PoolIdentityType,
    TaskState,
    TaskAddStatus,
    SubtaskState,
    StartTaskState,
    ComputeNodeState,
    SchedulingState,
    DisableJobOption,
    ComputeNodeDeallocationOption,
    ComputeNodeRebootOption,
    ComputeNodeReimageOption,
    DisableComputeNodeSchedulingOption,
)

__all__ = [
    'AccountListPoolNodeCountsOptions',
    'AccountListSupportedImagesOptions',
    'AffinityInformation',
    'ApplicationGetOptions',
    'ApplicationListOptions',
    'ApplicationPackageReference',
    'ApplicationSummary',
    'AuthenticationTokenSettings',
    'AutoPoolSpecification',
    'AutoScaleRun',
    'AutoScaleRunError',
    'AutoUserSpecification',
    'AzureBlobFileSystemConfiguration',
    'AzureFileShareConfiguration',
    'BatchError', 'BatchErrorException',
    'BatchErrorDetail',
    'BatchPoolIdentity',
    'Certificate',
    'CertificateAddOptions',
    'CertificateAddParameter',
    'CertificateCancelDeletionOptions',
    'CertificateDeleteOptions',
    'CertificateGetOptions',
    'CertificateListOptions',
    'CertificateReference',
    'CIFSMountConfiguration',
    'CloudJob',
    'CloudJobSchedule',
    'CloudPool',
    'CloudServiceConfiguration',
    'CloudTask',
    'CloudTaskListSubtasksResult',
    'ComputeNode',
    'ComputeNodeAddUserOptions',
    'ComputeNodeDeleteUserOptions',
    'ComputeNodeDisableSchedulingOptions',
    'ComputeNodeEnableSchedulingOptions',
    'ComputeNodeEndpointConfiguration',
    'ComputeNodeError',
    'ComputeNodeExtensionGetOptions',
    'ComputeNodeExtensionListOptions',
    'ComputeNodeGetOptions',
    'ComputeNodeGetRemoteDesktopOptions',
    'ComputeNodeGetRemoteLoginSettingsOptions',
    'ComputeNodeGetRemoteLoginSettingsResult',
    'ComputeNodeIdentityReference',
    'ComputeNodeInformation',
    'ComputeNodeListOptions',
    'ComputeNodeRebootOptions',
    'ComputeNodeReimageOptions',
    'ComputeNodeUpdateUserOptions',
    'ComputeNodeUploadBatchServiceLogsOptions',
    'ComputeNodeUser',
    'ContainerConfiguration',
    'ContainerRegistry',
    'DataDisk',
    'DeleteCertificateError',
    'DiffDiskSettings',
    'DiskEncryptionConfiguration',
    'EnvironmentSetting',
    'ErrorMessage',
    'ExitCodeMapping',
    'ExitCodeRangeMapping',
    'ExitConditions',
    'ExitOptions',
    'FileDeleteFromComputeNodeOptions',
    'FileDeleteFromTaskOptions',
    'FileGetFromComputeNodeOptions',
    'FileGetFromTaskOptions',
    'FileGetPropertiesFromComputeNodeOptions',
    'FileGetPropertiesFromTaskOptions',
    'FileListFromComputeNodeOptions',
    'FileListFromTaskOptions',
    'FileProperties',
    'HttpHeader',
    'ImageInformation',
    'ImageReference',
    'InboundEndpoint',
    'InboundNATPool',
    'InstanceViewStatus',
    'JobAddOptions',
    'JobAddParameter',
    'JobConstraints',
    'JobDeleteOptions',
    'JobDisableOptions',
    'JobDisableParameter',
    'JobEnableOptions',
    'JobExecutionInformation',
    'JobGetAllLifetimeStatisticsOptions',
    'JobGetOptions',
    'JobGetTaskCountsOptions',
    'JobListFromJobScheduleOptions',
    'JobListOptions',
    'JobListPreparationAndReleaseTaskStatusOptions',
    'JobManagerTask',
    'JobNetworkConfiguration',
    'JobPatchOptions',
    'JobPatchParameter',
    'JobPreparationAndReleaseTaskExecutionInformation',
    'JobPreparationTask',
    'JobPreparationTaskExecutionInformation',
    'JobReleaseTask',
    'JobReleaseTaskExecutionInformation',
    'JobScheduleAddOptions',
    'JobScheduleAddParameter',
    'JobScheduleDeleteOptions',
    'JobScheduleDisableOptions',
    'JobScheduleEnableOptions',
    'JobScheduleExecutionInformation',
    'JobScheduleExistsOptions',
    'JobScheduleGetOptions',
    'JobScheduleListOptions',
    'JobSchedulePatchOptions',
    'JobSchedulePatchParameter',
    'JobScheduleStatistics',
    'JobScheduleTerminateOptions',
    'JobScheduleUpdateOptions',
    'JobScheduleUpdateParameter',
    'JobSchedulingError',
    'JobSpecification',
    'JobStatistics',
    'JobTerminateOptions',
    'JobTerminateParameter',
    'JobUpdateOptions',
    'JobUpdateParameter',
    'LinuxUserConfiguration',
    'MetadataItem',
    'MountConfiguration',
    'MultiInstanceSettings',
    'NameValuePair',
    'NetworkConfiguration',
    'NetworkSecurityGroupRule',
    'NFSMountConfiguration',
    'NodeAgentInformation',
    'NodeCounts',
    'NodeDisableSchedulingParameter',
    'NodeFile',
    'NodePlacementConfiguration',
    'NodeRebootParameter',
    'NodeReimageParameter',
    'NodeRemoveParameter',
    'NodeUpdateUserParameter',
    'NodeVMExtension',
    'OSDisk',
    'OutputFile',
    'OutputFileBlobContainerDestination',
    'OutputFileDestination',
    'OutputFileUploadOptions',
    'PoolAddOptions',
    'PoolAddParameter',
    'PoolDeleteOptions',
    'PoolDisableAutoScaleOptions',
    'PoolEnableAutoScaleOptions',
    'PoolEnableAutoScaleParameter',
    'PoolEndpointConfiguration',
    'PoolEvaluateAutoScaleOptions',
    'PoolEvaluateAutoScaleParameter',
    'PoolExistsOptions',
    'PoolGetAllLifetimeStatisticsOptions',
    'PoolGetOptions',
    'PoolInformation',
    'PoolListOptions',
    'PoolListUsageMetricsOptions',
    'PoolNodeCounts',
    'PoolPatchOptions',
    'PoolPatchParameter',
    'PoolRemoveNodesOptions',
    'PoolResizeOptions',
    'PoolResizeParameter',
    'PoolSpecification',
    'PoolStatistics',
    'PoolStopResizeOptions',
    'PoolUpdatePropertiesOptions',
    'PoolUpdatePropertiesParameter',
    'PoolUsageMetrics',
    'PublicIPAddressConfiguration',
    'RecentJob',
    'ResizeError',
    'ResourceFile',
    'ResourceStatistics',
    'Schedule',
    'StartTask',
    'StartTaskInformation',
    'SubtaskInformation',
    'TaskAddCollectionOptions',
    'TaskAddCollectionParameter',
    'TaskAddCollectionResult',
    'TaskAddOptions',
    'TaskAddParameter',
    'TaskAddResult',
    'TaskConstraints',
    'TaskContainerExecutionInformation',
    'TaskContainerSettings',
    'TaskCounts',
    'TaskCountsResult',
    'TaskDeleteOptions',
    'TaskDependencies',
    'TaskExecutionInformation',
    'TaskFailureInformation',
    'TaskGetOptions',
    'TaskIdRange',
    'TaskInformation',
    'TaskListOptions',
    'TaskListSubtasksOptions',
    'TaskReactivateOptions',
    'TaskSchedulingPolicy',
    'TaskSlotCounts',
    'TaskStatistics',
    'TaskTerminateOptions',
    'TaskUpdateOptions',
    'TaskUpdateParameter',
    'UploadBatchServiceLogsConfiguration',
    'UploadBatchServiceLogsResult',
    'UsageStatistics',
    'UserAccount',
    'UserAssignedIdentity',
    'UserIdentity',
    'VirtualMachineConfiguration',
    'VirtualMachineInfo',
    'VMExtension',
    'VMExtensionInstanceView',
    'WindowsConfiguration',
    'WindowsUserConfiguration',
    'ApplicationSummaryPaged',
    'PoolUsageMetricsPaged',
    'CloudPoolPaged',
    'ImageInformationPaged',
    'PoolNodeCountsPaged',
    'CloudJobPaged',
    'JobPreparationAndReleaseTaskExecutionInformationPaged',
    'CertificatePaged',
    'NodeFilePaged',
    'CloudJobSchedulePaged',
    'CloudTaskPaged',
    'ComputeNodePaged',
    'NodeVMExtensionPaged',
    'OSType',
    'VerificationType',
    'AccessScope',
    'CertificateState',
    'CertificateFormat',
    'ContainerWorkingDirectory',
    'JobAction',
    'DependencyAction',
    'AutoUserScope',
    'ElevationLevel',
    'LoginMode',
    'OutputFileUploadCondition',
    'ComputeNodeFillType',
    'CertificateStoreLocation',
    'CertificateVisibility',
    'CachingType',
    'StorageAccountType',
    'DiskEncryptionTarget',
    'NodePlacementPolicyType',
    'DiffDiskPlacement',
    'DynamicVNetAssignmentScope',
    'InboundEndpointProtocol',
    'NetworkSecurityGroupRuleAccess',
    'IPAddressProvisioningType',
    'NodeCommunicationMode',
    'PoolLifetimeOption',
    'OnAllTasksComplete',
    'OnTaskFailure',
    'JobScheduleState',
    'ErrorCategory',
    'JobState',
    'JobPreparationTaskState',
    'TaskExecutionResult',
    'JobReleaseTaskState',
    'ContainerType',
    'StatusLevelTypes',
    'PoolState',
    'AllocationState',
    'PoolIdentityType',
    'TaskState',
    'TaskAddStatus',
    'SubtaskState',
    'StartTaskState',
    'ComputeNodeState',
    'SchedulingState',
    'DisableJobOption',
    'ComputeNodeDeallocationOption',
    'ComputeNodeRebootOption',
    'ComputeNodeReimageOption',
    'DisableComputeNodeSchedulingOption',
]
