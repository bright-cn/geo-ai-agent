<p align="center">
  <a href="https://www.bright.cn/">
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/brightdata/logo/light.svg" width="300" alt="Bright Data 标志">
  </a>
</p>

<div align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue"/>
  <img src="https://img.shields.io/badge/License-MIT-blue"/>
</div>

---

# 🚀 GEO AI Crew

GEO Agent Crew 使用 [CrewAI](https://crewai.com) 来自动执行由 AI 驱动的网页内容审计。输入一个 URL，系统将访问网页、提取标题、使用 [带有 Google Search 工具的 Gemini](https://ai.google.dev/gemini-api/docs/google-search) 生成并汇总相关查询，通过 [Bright Data SERP API](https://www.bright.cn/products/serp-api) 获取 Google AI Overviews，对比结果，并以 Markdown 文件输出可执行的页面级优化建议。

<img src="https://github.com/bright-cn/geo-ai-agent/blob/main/GEO%20diagram.png"/>

---

## 🤖 了解你的 Crew

ai-content-optimization-agent Crew 由六个 AI 代理组成，每个代理都有独特的角色、目标和工具。这些代理协作完成在 config/tasks.yaml 中定义的一系列任务，利用集体能力实现复杂目标。config/agents.yaml 文件概述了每个代理在你的 Crew 中的能力与配置。

## 🛠️ 安装

请确保系统已安装 Python >=3.10 且 <3.14。

本项目使用 [`uv`](https://docs.astral.sh/uv/) 进行依赖管理与包处理。
首先，如果尚未安装 uv，请运行：

```bash
pip install uv
```

然后，进入项目目录并安装项目依赖：

```bash
cd geo-ai-agent
uv sync
```

---

## 🔑 环境配置

本项目需要配置以下四个环境变量：
- GEMINI_API_KEY：你的 Gemini API Key
- MODEL：为代理 Crew 提供能力的 Gemini 模型名称（例如：gemini/gemini-2.5-flash）
- BRIGHT_DATA_API_KEY：你的 [Bright Data API key](https://docs.brightdata.com/api-reference/authentication)
- BRIGHT_DATA_ZONE：你要连接的 [Bright Data 仪表盘中的 Web Unlocker 区域](https://docs.brightdata.com/scraping-automation/web-unlocker/quickstart) 名称

你可以在终端中直接设置它们，或在项目根目录放置一个 .env 文件：
```
geo-ai-agent/
├── ...
├── .env # <---
└── src/
    └── ai_content_optimization_agent/
        └── ...
```
以如下方式填充 .env 文件：
```
GEMINI_API_KEY="<YOUR_GEMINI_API_KEY>"
MODEL="<CHOSEN_GEMINI_MODEL>"
BRIGHT_DATA_API_KEY="<BRIGHT_DATA_API_KEY>"
BRIGHT_DATA_ZONE="<YOUR_BRIGHT_DATA_ZONE>"
```

## ▶️ 运行项目
激活 uv sync 命令创建的 .venv：
```bash
 source .venv/bin/activate
```
在 Windows 上：
```powershell
.venv/Scripts/activate
```

激活虚拟环境后，在项目根目录运行以下命令启动你的 AI 代理 Crew：

```bash
crewai run
```

该命令会初始化 ai-content-optimization-agent Crew，按 CrewAI 配置文件组装代理并分配任务。

☑️ 应用将生成 output/report.md 文件，以及其他 output/*.md 文件，包含代理的中间数据与结果。

---

### ⚙️ 自定义
- 🔧 修改环境变量 MODEL 以更换该 Crew 使用的 Gemini 模型
- 🧑‍💻 编辑 `src/ai_content_optimization_agent/config/agents.yaml` 以调整代理定义
- 📋 编辑 `src/ai_content_optimization_agent/config/tasks.yaml` 以调整分配给代理的任务
- 🛠️ 更新 `src/ai_content_optimization_agent/crew.py` 以集成其他 AI 模型或加入自定义逻辑与工具
- ⚡ 编辑 `src/ai_content_optimization_agent/main.py` 为代理与任务添加自定义输入

---

## 💬 支持

如需关于 ai-content-optimization-agent Crew 或 CrewAI 的支持、问题或反馈：

- ☀️ 查看 Bright Data 的 [SERP API 文档](https://docs.brightdata.com/scraping-automation/serp-api/introduction)
- 📖 查看 CrewAI 的 [官方文档](https://docs.crewai.com)
- 🐙 通过 [GitHub 仓库](https://github.com/joaomdmoura/crewai) 联系 CrewAI
- 💬 [加入 Discord](https://discord.com/invite/X4JWnZnxPb)
- 💡 [与 CrewAI 文档对话](https://chatg.pt/DWjSBZn)

---

✨ 借助 Bright Data 与 CrewAI 的强大与简洁，让我们一起创造奇迹。
