# WorkBuddy 安装说明

## 最简单的安装方式

1. 打开 WorkBuddy 左侧的“专家·技能·连接器”。
2. 选择“添加技能”→“上传技能”。
3. 上传 `ad-planning-copilot-cn.workbuddy.zip`，完成后开一个新对话即可使用。

验证方式：输入“请拆解这份广告 Brief，先给我核心问题和策略主线”，应自动匹配本 Skill。也可输入 `/ad-planning-copilot-cn` 显式调用。

## 手动安装（备选）

将解压后的 `ad-planning-copilot-cn` 整个文件夹放入：

- 用户级（所有项目可用）：`~/.workbuddy/skills/ad-planning-copilot-cn/`
- 项目级（仅当前项目可用）：`{项目目录}/.workbuddy/skills/ad-planning-copilot-cn/`

确保 `SKILL.md` 直接位于该文件夹根目录。若技能列表未更新，刷新或重启 WorkBuddy。

## 使用提示

- 简单任务直接说需求，如“把这页标题改得更像策略判断”。
- 需要模式切换时，可用 `#策略` 或 `#创意`。
- 需要多方向时明确说“发散 3 个不同方向”；否则默认先给 1 个完成度高的答案。
- 需要联网洞察时，WorkBuddy 本机还需有可用的浏览器/搜索能力；本包不携带任何账号登录态、Cookie 或 API Key。
- Agent Reach 的调研路由已包含。如同事电脑已安装运行组件，可在 WorkBuddy 中输入“运行 `agent-reach doctor --json` 检查联网能力”；未安装时仍可使用 WorkBuddy 自带的只读浏览器/搜索能力。

## 许可提醒

`songyue-insight` 和 `songyue-marketingdx` 仅可非商业使用，商业客户项目须先取得作者书面授权。未授权时，主 Skill 会使用内置的基础洞察与诊断流程，不会调用这两个受限模块。完整说明见 `THIRD-PARTY-NOTICES.md`。
