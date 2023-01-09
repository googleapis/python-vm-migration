# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.vmmigration import gapic_version as package_version

__version__ = package_version.__version__


from .services.vm_migration import VmMigrationAsyncClient, VmMigrationClient
from .types.vmmigration import (
    AdaptingOSStep,
    AddGroupMigrationRequest,
    AddGroupMigrationResponse,
    ApplianceVersion,
    AppliedLicense,
    AvailableUpdates,
    AwsSecurityGroup,
    AwsSourceDetails,
    AwsSourceVmDetails,
    AwsVmDetails,
    AwsVmsDetails,
    CancelCloneJobRequest,
    CancelCloneJobResponse,
    CancelCutoverJobRequest,
    CancelCutoverJobResponse,
    CloneJob,
    CloneStep,
    ComputeEngineBootOption,
    ComputeEngineDiskType,
    ComputeEngineLicenseType,
    ComputeEngineTargetDefaults,
    ComputeEngineTargetDetails,
    ComputeScheduling,
    CreateCloneJobRequest,
    CreateCutoverJobRequest,
    CreateDatacenterConnectorRequest,
    CreateGroupRequest,
    CreateMigratingVmRequest,
    CreateSourceRequest,
    CreateTargetProjectRequest,
    CreateUtilizationReportRequest,
    CutoverJob,
    CutoverStep,
    CycleStep,
    DatacenterConnector,
    DeleteDatacenterConnectorRequest,
    DeleteGroupRequest,
    DeleteMigratingVmRequest,
    DeleteSourceRequest,
    DeleteTargetProjectRequest,
    DeleteUtilizationReportRequest,
    FetchInventoryRequest,
    FetchInventoryResponse,
    FinalizeMigrationRequest,
    FinalizeMigrationResponse,
    GetCloneJobRequest,
    GetCutoverJobRequest,
    GetDatacenterConnectorRequest,
    GetGroupRequest,
    GetMigratingVmRequest,
    GetReplicationCycleRequest,
    GetSourceRequest,
    GetTargetProjectRequest,
    GetUtilizationReportRequest,
    Group,
    InitializingReplicationStep,
    InstantiatingMigratedVMStep,
    ListCloneJobsRequest,
    ListCloneJobsResponse,
    ListCutoverJobsRequest,
    ListCutoverJobsResponse,
    ListDatacenterConnectorsRequest,
    ListDatacenterConnectorsResponse,
    ListGroupsRequest,
    ListGroupsResponse,
    ListMigratingVmsRequest,
    ListMigratingVmsResponse,
    ListReplicationCyclesRequest,
    ListReplicationCyclesResponse,
    ListSourcesRequest,
    ListSourcesResponse,
    ListTargetProjectsRequest,
    ListTargetProjectsResponse,
    ListUtilizationReportsRequest,
    ListUtilizationReportsResponse,
    MigratingVm,
    MigratingVmView,
    MigrationError,
    NetworkInterface,
    OperationMetadata,
    PauseMigrationRequest,
    PauseMigrationResponse,
    PostProcessingStep,
    PreparingVMDisksStep,
    RemoveGroupMigrationRequest,
    RemoveGroupMigrationResponse,
    ReplicatingStep,
    ReplicationCycle,
    ReplicationSync,
    ResumeMigrationRequest,
    ResumeMigrationResponse,
    SchedulePolicy,
    SchedulingNodeAffinity,
    ShuttingDownSourceVMStep,
    Source,
    StartMigrationRequest,
    StartMigrationResponse,
    TargetProject,
    UpdateGroupRequest,
    UpdateMigratingVmRequest,
    UpdateSourceRequest,
    UpdateTargetProjectRequest,
    UpgradeApplianceRequest,
    UpgradeApplianceResponse,
    UpgradeStatus,
    UtilizationReport,
    UtilizationReportView,
    VmUtilizationInfo,
    VmUtilizationMetrics,
    VmwareSourceDetails,
    VmwareVmDetails,
    VmwareVmsDetails,
)

__all__ = (
    "VmMigrationAsyncClient",
    "AdaptingOSStep",
    "AddGroupMigrationRequest",
    "AddGroupMigrationResponse",
    "ApplianceVersion",
    "AppliedLicense",
    "AvailableUpdates",
    "AwsSecurityGroup",
    "AwsSourceDetails",
    "AwsSourceVmDetails",
    "AwsVmDetails",
    "AwsVmsDetails",
    "CancelCloneJobRequest",
    "CancelCloneJobResponse",
    "CancelCutoverJobRequest",
    "CancelCutoverJobResponse",
    "CloneJob",
    "CloneStep",
    "ComputeEngineBootOption",
    "ComputeEngineDiskType",
    "ComputeEngineLicenseType",
    "ComputeEngineTargetDefaults",
    "ComputeEngineTargetDetails",
    "ComputeScheduling",
    "CreateCloneJobRequest",
    "CreateCutoverJobRequest",
    "CreateDatacenterConnectorRequest",
    "CreateGroupRequest",
    "CreateMigratingVmRequest",
    "CreateSourceRequest",
    "CreateTargetProjectRequest",
    "CreateUtilizationReportRequest",
    "CutoverJob",
    "CutoverStep",
    "CycleStep",
    "DatacenterConnector",
    "DeleteDatacenterConnectorRequest",
    "DeleteGroupRequest",
    "DeleteMigratingVmRequest",
    "DeleteSourceRequest",
    "DeleteTargetProjectRequest",
    "DeleteUtilizationReportRequest",
    "FetchInventoryRequest",
    "FetchInventoryResponse",
    "FinalizeMigrationRequest",
    "FinalizeMigrationResponse",
    "GetCloneJobRequest",
    "GetCutoverJobRequest",
    "GetDatacenterConnectorRequest",
    "GetGroupRequest",
    "GetMigratingVmRequest",
    "GetReplicationCycleRequest",
    "GetSourceRequest",
    "GetTargetProjectRequest",
    "GetUtilizationReportRequest",
    "Group",
    "InitializingReplicationStep",
    "InstantiatingMigratedVMStep",
    "ListCloneJobsRequest",
    "ListCloneJobsResponse",
    "ListCutoverJobsRequest",
    "ListCutoverJobsResponse",
    "ListDatacenterConnectorsRequest",
    "ListDatacenterConnectorsResponse",
    "ListGroupsRequest",
    "ListGroupsResponse",
    "ListMigratingVmsRequest",
    "ListMigratingVmsResponse",
    "ListReplicationCyclesRequest",
    "ListReplicationCyclesResponse",
    "ListSourcesRequest",
    "ListSourcesResponse",
    "ListTargetProjectsRequest",
    "ListTargetProjectsResponse",
    "ListUtilizationReportsRequest",
    "ListUtilizationReportsResponse",
    "MigratingVm",
    "MigratingVmView",
    "MigrationError",
    "NetworkInterface",
    "OperationMetadata",
    "PauseMigrationRequest",
    "PauseMigrationResponse",
    "PostProcessingStep",
    "PreparingVMDisksStep",
    "RemoveGroupMigrationRequest",
    "RemoveGroupMigrationResponse",
    "ReplicatingStep",
    "ReplicationCycle",
    "ReplicationSync",
    "ResumeMigrationRequest",
    "ResumeMigrationResponse",
    "SchedulePolicy",
    "SchedulingNodeAffinity",
    "ShuttingDownSourceVMStep",
    "Source",
    "StartMigrationRequest",
    "StartMigrationResponse",
    "TargetProject",
    "UpdateGroupRequest",
    "UpdateMigratingVmRequest",
    "UpdateSourceRequest",
    "UpdateTargetProjectRequest",
    "UpgradeApplianceRequest",
    "UpgradeApplianceResponse",
    "UpgradeStatus",
    "UtilizationReport",
    "UtilizationReportView",
    "VmMigrationClient",
    "VmUtilizationInfo",
    "VmUtilizationMetrics",
    "VmwareSourceDetails",
    "VmwareVmDetails",
    "VmwareVmsDetails",
)
