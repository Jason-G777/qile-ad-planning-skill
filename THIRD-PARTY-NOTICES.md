# 第三方来源与许可

本包是一个聚合式 Skill，原始模块作为独立组件保留在 `references/modules/` 中。各模块仍适用其各自许可，不因被打包而改变。

## songyue-insight

- 作者：Songyue / 宋玥
- 许可：CC BY-NC-SA 4.0
- 商业使用：需作者单独书面授权
- 原始许可与声明：`references/modules/songyue-insight/LICENSE` 和 `references/modules/songyue-insight/NOTICE`

## songyue-marketingdx

- 作者：Songyue / 宋玥
- 许可：CC BY-NC-SA 4.0
- 商业使用：需作者单独书面授权
- 原始声明：`references/modules/songyue-marketingdx/NOTICE`

## planners-quali-box

- 作者/维护者：阿祖不看 TVC
- 项目站点：https://demyth.info
- 许可：GNU AGPL-3.0
- 商业使用：允许，但须遵守 AGPL-3.0 的源码开放义务；闭源商业授权可联系 `Lawyif@163.com`
- 原始许可与声明：`references/modules/planners-quali-box/LICENSE`、`NOTICE`、`COMMERCIAL.md`

## genz-insight-radar

该模块来自当前策划工作区。本包不携带任何小红书或其他平台的账号登录态、Cookie 或个人信息。每位使用者必须使用自己的账号和已授权工具，且仅执行只读采集。

## agent-reach

- 作者：Neo Reid / Panniantong
- 项目：https://github.com/Panniantong/Agent-Reach
- 集成版本：1.5.0 对应的 Skill 路由文档
- 许可：MIT
- 原始许可：`references/modules/agent-reach/LICENSE`
- 本包只集成 Skill 路由文档，不携带用户 Cookie、API Key、浏览器登录态或跨平台命令行组件。

## humanizer

- 作者：Siqi Chen
- 项目：https://github.com/blader/humanizer
- 集成版本：2.7.0
- 许可：MIT
- 商业使用：允许
- 原始许可与说明：`references/modules/humanizer/LICENSE` 和 `references/modules/humanizer/README.md`
- 本整合包保留原始Skill全文，在主入口增加广告策划场景的调用边界；不改变原项目归属或许可。

## 聚合包修改说明

- 2026-09-11：将上述模块作为独立参考组件集成到 `ad-planning-copilot-cn`；新增统一任务路由、身份设定、案例机制库和 WorkBuddy 本地安装说明。同日增加 Agent Reach 联网调研路由及 MIT 许可文件。
- 2026-09-22：新增 Humanizer 2.7.0，用于文案去AI味、声音校准与二次语言质检；主入口增加广告场景适配，避免语言清理覆盖策略、事实与有意的品牌表达。
- 未删除各第三方模块的原始归属、许可或声明。
