# Hello_World 完善方案（Improvement Plan）

> 状态：提案，待维护者确认
> 提交方式：以 PR 新增本文件，不改变现有代码
> 基准：`master` @ `aa22424`（PR #2 合并后，2026-11-04）
> 关联讨论：[#3](https://github.com/xxb0120/Hello_World/issues/3)（仓库应包含哪些内容）、[#4](https://github.com/xxb0120/Hello_World/issues/4)（Java 示例）

## 摘要

仓库目前只有一份 Python 3.8+ 的 Hello World 脚本、7 个 `unittest` 用例和一份 README：**能跑、能测，但缺少仓库层面的工程基线**——没有 LICENSE、没有 CI、没有贡献指南，也没有“新增一个语言示例”的统一结构（见 #3）。

本方案建议把定位收敛为 **多语言 Hello World 示例集 + 统一工程基线**：每个语言一个自包含目录（源码 + 测试 + 运行说明），仓库级统一提供 LICENSE、CI、README 索引和贡献指南。按 P0–P3 四步推进，总工作量约 2–3 人日：

1. **P0 工程基线**（0.5–1 人日）：LICENSE、GitHub Actions CI、README 索引、CONTRIBUTING。
2. **P1 结构统一**（0.2 人日）：现有 Python 示例迁入 `examples/python/`。
3. **P2 第二语言**（0.4 人日）：`examples/java/`，同时收尾 #1/#3/#4。
4. **P3 质量门禁**（0.3 人日）：ruff 格式与检查接入 CI。

每步都可独立提交 PR、独立回滚，不改变现有 Python 程序的行为。

## 1. 现状盘点

| 维度 | 现状 | 问题 |
| --- | --- | --- |
| 内容 | 1 个 Python 示例 `hello_world.py`（1367 B） | 只有一种语言；#4 的 Java 示例尚未开始 |
| 测试 | `test_hello_world.py`：7 个 `unittest` 用例 + doctest | 只在本地跑，合并前无自动校验，回归只能靠人工 |
| 文档 | 单份根 `README.md`（388 B） | 有用法与测试命令，但没有仓库索引、没有“如何新增示例”的约定 |
| 工程基线 | 无 | 无 LICENSE（默认版权保留，他人复用有法律不确定性）、无 CI、无 lint/format 配置、无 issue/PR 模板 |
| 分支与发布 | 仅 `master`，无 tag | 没有发布节奏；对示例仓库可接受，暂不作为目标 |
| 问题跟踪 | #1、#3、#4 均开放 | #1（编写 Python 程序）已由合并的 PR #2 覆盖，可以关闭；#3 正是本方案要回答的问题；#4 纳入 P2 |

已核实（2026-11-04，Python 3.10.10，`master` @ `aa22424`）：

```console
$ python3 hello_world.py
Hello, World!
$ python3 hello_world.py Alice
Hello, Alice!
$ python3 hello_world.py " "    # 空名字
error: name must not be empty    # exit code 2
$ python3 -m unittest -v
Ran 7 tests ... OK
$ python3 -m doctest hello_world.py   # 无输出即通过
```

这些行为是本方案的兼容性基线：P0–P3 不应改变它们（迁移目录时需同步更新路径，见 P1）。

## 2. 定位与原则

**定位：多语言 Hello World 示例集。** 每个示例回答三个问题：怎么运行、怎么测试、怎么再加一个语言。仓库不追求功能深度，追求“打开任意一个目录就能在 1 分钟内跑起来”。

**原则：**

- **最小依赖**：示例优先使用语言标准库；不引入 Web 框架、数据库、容器化。
- **一个语言一个目录**：结构、命名、命令保持一致，新增语言是复制模板而不是发明结构。
- **测试随示例走**：每个示例至少有一个自动测试（单元测试或输出冒烟测试），并接入 CI。
- **仓库级只放共性文件**：README、LICENSE、CONTRIBUTING、CI 配置。
- **能删就删**：不为示例仓库引入发布流水线、覆盖率门槛、多环境矩阵等重型设施。

**非目标（明确不做）：**

- 不做服务化 / Web 应用 / 部署脚本；
- 不发布到 PyPI、Maven Central 等包仓库；
- 不为每个语言堆功能（每个示例 ≤ 1 个可运行入口 + 1 个测试文件）；
- 不追求覆盖率百分比或性能基准；
- 暂不引入 Java 之外的第二种 JVM 语言或框架。

## 3. 目标结构

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml              # P0：Python 测试 + doctest + CLI 冒烟；P2 增加 Java 任务
├── docs/
│   └── IMPROVEMENT_PLAN.md     # 本文件
├── examples/
│   ├── python/
│   │   ├── README.md           # 运行/测试命令
│   │   ├── hello_world.py
│   │   └── test_hello_world.py
│   └── java/                   # P2（#4）
│       ├── README.md
│       └── HelloWorld.java
├── .gitignore
├── CONTRIBUTING.md             # P0：如何新增语言示例、如何提交
├── LICENSE                     # P0：MIT（待 D3 确认）
└── README.md                   # 索引页：语言、入口文件、运行命令、测试命令
```

根 README 建议改成三段：**这是什么 → 快速开始（一条命令跑起来）→ 示例索引表**，索引表每行一个语言，列为「语言 / 入口 / 运行 / 测试」。这样 #3 的问题在首页就能回答。

## 4. 工作项

### 总览

| ID | 工作项 | 优先级 | 预估 | 依赖 | 验收标准 |
| --- | --- | --- | --- | --- | --- |
| P0-1 | 添加 `LICENSE` | P0 | 0.1 人日 | D3 | 文件存在，GitHub 仓库页显示 MIT |
| P0-2 | 添加 GitHub Actions CI | P0 | 0.3 人日 | D5、D6 | PR 上自动运行；Python 测试、doctest、CLI 冒烟全绿 |
| P0-3 | 重构根 `README.md` 为索引页 | P0 | 0.2 人日 | D2 | 一屏内能回答“跑哪个、怎么跑、怎么测、怎么加语言” |
| P0-4 | 添加 `CONTRIBUTING.md` | P0 | 0.1 人日 | D2 | 包含新增示例的目录规范、测试要求、PR 检查项 |
| P1-1 | 现有 Python 示例迁入 `examples/python/` | P1 | 0.2 人日 | D2 | 迁移后测试与 doctest 仍通过；README 与引用路径同步更新 |
| P2-1 | 新增 Java 示例（#4） | P1 | 0.3 人日 | D4 | `examples/java/` 可按 README 运行；CI 冒烟通过 |
| P2-2 | 收尾开放 issue | P2 | 0.1 人日 | 无 | #1 关闭；#3 链接本方案；#4 标记为已完成/已排期 |
| P3-1 | Python lint/format 接入 CI | P2 | 0.3 人日 | 无 | `ruff check`、`ruff format --check` 在 CI 中通过 |
| P3-2 | 可选：mypy、pre-commit、覆盖率 | P3 | 0.3 人日 | 有需要时 | 不阻塞主流程，按需引入 |

### P0-1 添加 LICENSE

- **做什么**：根目录添加 `LICENSE`（建议 MIT，见 D3），README 末尾加 License 小节。
- **为什么**：当前无许可证，默认“保留所有权利”，他人复制、修改、再发布存在法律不确定性。对“示例仓库”来说这是最便宜、收益最高的补齐项。
- **验收**：GitHub 仓库页右侧显示 MIT；`LICENSE` 中的年份与版权人正确。

### P0-2 添加 GitHub Actions CI

- **做什么**：新增 `.github/workflows/ci.yml`，在 `push` 到 `master` 和所有 `pull_request` 上运行 Python 任务：

```yaml
name: CI
on:
  push:
    branches: [master]
  pull_request:

permissions:
  contents: read

jobs:
  python:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.11", "3.12", "3.13", "3.14"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Unit tests
        run: python -m unittest discover -s examples/python -v
      - name: Doctests
        run: python -m doctest examples/python/hello_world.py
      - name: CLI smoke test
        run: |
          test "$(python examples/python/hello_world.py)" = "Hello, World!"
          test "$(python examples/python/hello_world.py Alice)" = "Hello, Alice!"
```

- **为什么**：现在合并前没有任何自动校验，回归只能靠人工跑测试。CI 是后续所有改动（尤其是多语言）的安全网。
- **验收**：PR 上出现 CI 检查；故意改坏一个断言时 CI 变红；矩阵版本全部通过。
- **备注**：`matrix` 的版本范围与 D6 结论一致；若先做 P0 再做 P1，可把路径写成根目录，P1 迁移时同步改 `examples/python`。

### P0-3 重构根 README 为索引页

- **做什么**：按以下顺序重写根 README：

  1. 一句话介绍（多语言 Hello World 示例集）；
  2. 快速开始：`python3 examples/python/hello_world.py`；
  3. 示例索引表：

     | 语言 | 入口 | 运行 | 测试 |
     | --- | --- | --- | --- |
     | Python 3.11+ | `examples/python/hello_world.py` | `python3 examples/python/hello_world.py [name]` | `python3 -m unittest discover -s examples/python` |
     | Java 21+ | `examples/java/HelloWorld.java` | `java examples/java/HelloWorld.java` | CI 冒烟 |

  4. 目录结构说明；
  5. 如何新增一个语言（链接 CONTRIBUTING）；
  6. License。

- **为什么**：当前 README 只服务 Python 一个示例；#3 的问题“仓库应该包含哪些内容”本质上需要一个首页来回答。
- **验收**：新人只看首页即可运行任意示例；索引表中的命令逐条实测可用；若 P1-1 尚未执行，路径先按当前根目录书写，并在迁移 PR 中同步更新。

### P0-4 添加 CONTRIBUTING.md

- **做什么**：写明新增语言示例的约定：目录 `examples/<language>/`、必须包含 `README.md`（运行与测试命令）和至少一个测试、命名用小写（如 `examples/go/hello_world.go`）、提交前跑通 CI；以及 PR 描述需包含“怎么验证”的命令与输出。
- **为什么**：多语言仓库的最大成本是结构漂移；一条写下来的约定能避免每个语言各长各的。
- **验收**：按文档从零加一个示例时，不需要额外询问结构问题。

### P1-1 现有 Python 示例迁入 `examples/python/`

- **做什么**：移动 `hello_world.py`、`test_hello_world.py` 到 `examples/python/`，新增 `examples/python/README.md`；同步更新根 README 引用、CI 路径、doctest 命令。
- **为什么**：统一结构的前提；趁仓库只有 4 个文件时一次迁移成本最低。
- **验收**：`python3 -m unittest discover -s examples/python -v` 与 `python3 -m doctest examples/python/hello_world.py` 通过；CI 全绿；根 README 无失效链接。
- **注意**：这是唯一的破坏性变更（文件路径变化）。执行前确认 D2；需要一次性提交完成，避免出现“两套路径并存”的中间态。

### P2-1 新增 Java 示例（#4）

- **做什么**：新增 `examples/java/HelloWorld.java`（JDK 21 单文件源码启动，无需构建工具）与 `examples/java/README.md`；CI 增加 Java 任务：

```yaml
# 追加到 ci.yml 的 jobs: 下
  java:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: "21"
      - name: Smoke test
        run: |
          test "$(java examples/java/HelloWorld.java)" = "Hello, World!"
```

- **为什么**：#4 已提出；Java 是示例仓库里最常被期待的第二语言；单文件方案不引入 Maven/Gradle 依赖，符合“最小依赖”原则。
- **验收**：`java examples/java/HelloWorld.java` 输出 `Hello, World!`；CI Java 任务通过；README 索引表新增一行。
- **备选**：若希望 Java 侧也做单元测试，改用 Maven + JUnit 5（见 D4），代价是多一个 `pom.xml` 和第三方依赖。

### P2-2 收尾开放 issue

- **做什么**：#1 在 PR #2 合并后已满足，可由维护者关闭并留言说明；#3 关联本方案；#4 在 P2-1 合并后关闭。
- **为什么**：开放 issue 是仓库的“待办清单”，不清理会掩盖真实进度。
- **验收**：#1/#4 关闭；#3 有指向本方案或后续 PR 的说明。

### P3-1 Python lint/format 接入 CI

- **做什么**：在 `pyproject.toml` 中只放工具配置（`[tool.ruff]`，不做打包），CI 增加 `ruff check` 与 `ruff format --check`；对现有代码先跑一遍 `ruff format`。
- **为什么**：格式统一可以让多语言示例的 review 聚焦在内容而非空格；ruff 单工具同时覆盖 lint 与 format，依赖成本低。
- **验收**：CI 中 ruff 步骤通过；本地 `ruff check .` 无告警。
- **注意**：首次引入时用默认规则集，避免一次性打开大量规则导致噪音。

## 5. 里程碑

| 里程碑 | 内容 | 产出 | 预计 |
| --- | --- | --- | --- |
| M1 可验证基线 | P0-1 ~ P0-4 | 有 LICENSE、CI、索引 README、贡献指南 | 第 1 天 |
| M2 结构统一 | P1-1 | 所有示例位于 `examples/` | 第 2 天 |
| M3 第二语言 | P2-1、P2-2 | Java 示例可运行，issue 收尾 | 第 2–3 天 |
| M4 质量门禁 | P3-1（P3-2 可选） | lint/format 进入 CI | 第 3 天 |

每个里程碑都可以在独立 PR 中完成；M1 与 M2 可以合并为一个 PR（约 1.2 人日），以降低 review 次数。

## 6. 需要维护者拍板的决策点

| 编号 | 决策 | 选项 | 建议 |
| --- | --- | --- | --- |
| D1 | 仓库定位 | A. 多语言示例集；B. 仅 Python 单语言示例；C. 教学/模板仓库 | **A**。与 #3、#4 的方向一致，且成本可控 |
| D2 | 是否迁移现有文件到 `examples/python/` | A. 迁移；B. Python 保留在根目录，新语言放 `examples/` | **A**。内容少时迁移最便宜；B 会造成长期结构不一致 |
| D3 | LICENSE 类型 | MIT / Apache-2.0 / 其他 | **MIT**。示例代码最常用，条款最短 |
| D4 | Java 构建方式 | A. 单文件源码启动；B. Maven + JUnit 5 | **A**。符合“最小依赖”；若需要 Java 单元测试再升级到 B |
| D5 | CI 是否作为合并门禁 | A. `master` 分支保护要求 CI 通过；B. 仅提示不阻塞 | **A**。对单人维护仓库也值得，避免“红了还合并” |
| D6 | Python 最低版本 | A. 保持 3.8+；B. 提升到 3.11+ | **B**。3.8 已于 2024-10 停止维护，3.9 于 2025-10、3.10 于 2026-10 停止维护；CI 覆盖 3.11–3.14 即可 |

> D1–D4 影响结构，建议在 M1 之前确认；D5 需要仓库管理员在 Settings → Branches 中配置；D6 只影响文档与 CI 矩阵。

## 7. 风险与应对

| 风险 | 影响 | 应对 |
| --- | --- | --- |
| 迁移目录破坏既有链接（README、issue 中的路径） | 低 | 一次性迁移 + 全仓搜索旧路径 + 在 PR 描述中标注破坏性变更 |
| CI 首次运行失败（action 版本、矩阵版本不可用） | 低 | 固定 action 主版本；先在分支验证再合并；`fail-fast: false` 便于定位 |
| 引入 ruff 后既有代码大量告警 | 中 | 先用默认规则集，只修 format 差异；规则收紧单独 PR |
| Java 单文件方案难以写单元测试 | 低 | 先用输出冒烟测试；确有需要再切 Maven |
| 范围膨胀（不断加语言/加功能） | 中 | 以本方案“非目标”为准；新增语言按需、按 issue 驱动 |
| 公开仓库 Actions 未启用或额度受限 | 低 | 维护者在 Settings → Actions 中启用；公开仓库标准 runner 免费 |

## 8. 总体验收标准

方案完成的标志（全部满足）：

1. 根 README 能在一屏内回答“怎么跑、怎么测、怎么加语言”，索引表命令逐条实测可用；
2. 每个示例目录自包含（源码 + 测试 + 运行说明），新增语言无需改动仓库级代码；
3. CI 在 PR 上自动运行 Python（及 Java，P2 后）检查并全绿；
4. 存在 `LICENSE` 与 `CONTRIBUTING.md`；
5. 开放 issue 均有归属（关闭或纳入里程碑）；
6. 现有 Python 程序的输出与退出码保持不变（`Hello, World!`、`Hello, Alice!`、空名字退出码 2）。

## 9. 建议的落地顺序

1. **PR 1（M1）**：LICENSE + `ci.yml`（Python）+ README 索引 + CONTRIBUTING。约 0.7–1 人日，不动代码路径，风险最低。若与 PR 2 拆开提交，PR 1 的 README 先按现有根目录路径编写，PR 2 迁移后同步更新。
2. **PR 2（M2）**：迁移到 `examples/python/`，同步 CI 与 README。约 0.2 人日。
3. **PR 3（M3）**：Java 示例 + CI Java 任务，关闭 #4。约 0.3 人日。
4. **PR 4（M4）**：ruff 接入 CI。约 0.3 人日。

每个 PR 独立可回滚；PR 1 完成后，后续任何一步都可以暂停而不影响仓库可用性。
