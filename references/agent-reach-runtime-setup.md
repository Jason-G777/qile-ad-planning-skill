# Agent Reach 在 Codex 中的运行时检查与修复

本文件只解决“Skill 已能被 Codex 读取，但 Agent Reach 命令或平台后端不可用”的问题。Agent Reach 官方要求 Python 3.10+；推荐 `pipx` 或独立 `venv`，不强制要求 Conda。

## 先分清三层

1. **策划 Skill**：告诉 Codex 什么任务应调用 Agent Reach。
2. **Agent Reach CLI**：提供 `install`、`doctor`、`configure` 等命令。
3. **平台后端**：OpenCLI、bili-cli、yt-dlp、mcporter、gh 等真正读取内容的上游工具。

安装了第一层，不代表第二、三层已经存在。不得把这一状态简称为“缺少 Conda 后端”。

## Codex 首次预检

在本 Skill 根目录执行：

```bash
# macOS / Linux
python3 scripts/agent_reach_preflight.py

# Windows PowerShell
py -3 scripts/agent_reach_preflight.py
```

脚本只读检查当前 Python、PATH、Agent Reach 和常用上游命令；发现 Agent Reach 后会调用 `agent-reach doctor --json`，不会安装软件、修改配置或读取 Cookie。

状态解释：

| 状态 | 含义 | 处理 |
|---|---|---|
| `ready` | CLI 可见，已返回 doctor 结果 | 只验证当前任务所需平台 |
| `runtime_missing` | 有 Skill 文档，没有 CLI | 按下文安装；若现有 Codex 浏览器足够，可先降级完成任务 |
| `path_not_visible` | 磁盘里找到 CLI，但 Codex 当前 PATH 看不到 | 使用结果中的 `detected_executable`，并重启 Codex |
| `doctor_failed` | CLI 存在，但 doctor 执行失败或超时 | 保留错误摘要，按官方安装文档修复，不猜原因 |

## 安装 Agent Reach CLI

安装会写入用户目录并下载软件。只有用户明确要求安装/修复，且 Codex 获得相应权限后执行。

先确认 Python：

```bash
# macOS / Linux
python3 --version

# Windows
py -3 --version
```

必须为 Python 3.10 或以上。官方优先推荐 `pipx`：

```bash
# GitHub 可访问
pipx install https://github.com/Panniantong/agent-reach/archive/main.zip

# 中国大陆或 GitHub 不稳定：官方 README 列出的 AtomGit 镜像
pipx install git+https://atomgit.com/qq_51337814/Agent-Reach.git
```

Windows 可直接通过 Python Launcher 调用 pipx，避免新 PATH 尚未生效：

```powershell
py -3 -m pip install --user pipx
py -3 -m pipx ensurepath
py -3 -m pipx install git+https://atomgit.com/qq_51337814/Agent-Reach.git
```

如果 macOS 的 Homebrew Python 提示 `externally-managed-environment`，不要强行向系统 Python 安装，使用 `pipx`；或者按官方方案建立隔离环境：

```bash
python3 -m venv ~/.agent-reach-venv
source ~/.agent-reach-venv/bin/activate
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
```

安装后关闭并重启 Codex，使新 PATH 生效。若 GitHub 不通且电脑没有 Git，可从 AtomGit 手动下载源码压缩包，再让 `pipx install` 指向本地压缩包或解压目录。

## 安装后分两步处理

先做只读检查：

```bash
agent-reach install --env=auto
agent-reach doctor --json
```

默认 `install --env=auto` 只列出缺失项，不修改系统。只有用户再次明确允许安装系统/外部组件时，才运行：

```bash
agent-reach install --env=auto --system
```

可先预览：

```bash
agent-reach install --env=auto --dry-run
```

不要为了让 doctor 全绿而安装所有平台。只安装当前工作真正需要的渠道。小红书、Twitter、Reddit、Facebook、Instagram 等还需要用户控制的浏览器登录态或 Cookie；不得把登录态放进 Skill 或 Git 仓库。

## Codex 中的降级规则

- 公开网页、普通搜索或 GitHub 公共内容：Codex 已有只读浏览器/搜索能力时可以直接继续，并说明没有启用哪些 Agent Reach 专用渠道。
- 小红书、Twitter/Reddit 登录内容、B站完整能力、字幕/播客转写：没有对应后端时不可假装已查；安装需要的单一渠道，或明确本轮证据缺口。
- `active_backend: null` 只表示 doctor 未完成实时验证的可能性之一。根据模块 reference 对当前目标执行一次只读命令，以非空结果作为验收。
- 安装完成不代表所有平台可用；成功标准是当前任务目标获得了真实、非空、可追溯的内容。

## 权威来源

- Agent Reach 官方安装文档：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
- Agent Reach 官方仓库：https://github.com/Panniantong/Agent-Reach
- 官方 README 列出的国内镜像：https://atomgit.com/qq_51337814/Agent-Reach
- Codex Agent Skills：https://developers.openai.com/codex/skills
