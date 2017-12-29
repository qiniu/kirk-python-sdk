# -*- coding: utf-8 -*-

KIRK_HOST_PRO = "https://keapi.qiniu.com"
KIRK_HOST_DEV = "https://keapi-cs.qiniu.io"

# 微服务类型
MicroServiceTypeStateful  = "stateful"  # 有状态
MicroServiceTypeStateless = "stateless" # 无状态

# 微服务状态
MicroServicePhaseRunning = "running"
MicroServicePhasePending = "pending"
MicroServicePhaseStopped = "stopped"
MicroServicePhaseUnknown = "unknown"

# 容器状态
ContainerStateRunning    = "running"
ContainerStateWaiting    = "waiting"
ContainerStateTerminated = "terminated"
ContainerStateUnknown    = "unknown"

ProtocolTypeTCP = "TCP"
ProtocolTypeUDP = "UDP"