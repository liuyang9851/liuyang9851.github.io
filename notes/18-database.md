# 数据库系统概论

## SQL部分

Structured Query Language 结构化查询语言

* DDL：数据定义语言
* DML：数据操纵语言
* DCL：数据控制语言

| SQL功能  | 动词                   |
| -------- | ---------------------- |
| 数据查询 | SELECT                 |
| 数据定义 | CREATE，DROP，ALTER    |
| 数据操纵 | INSERT，UPDATE，DELETE |
| 数据控制 | GRANT，REVOKE          |

### 速查表

| 关键字                   | 含义 / 作用                                                                                                    |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `ADD`                  | `ALTER TABLE` 中用于增加列或表级约束                                                                         |
| `AFTER`                | 触发器时机：在触发事件**之后**执行动作体                                                                 |
| `ALL`                  | ①`SELECT` 中返回所有行（含重复，默认）<br />② 量化比较中表示“大于/小于/等于**所有**子查询结果”     |
| `ALTER`                | 修改数据库对象定义（如 `ALTER TABLE`、`ALTER INDEX`）                                                      |
| `ALTER INDEX`          | 修改索引（如重命名）                                                                                           |
| `ALTER TABLE`          | 修改表结构（增加/删除列、修改数据类型、增删约束）                                                              |
| `AND`                  | 逻辑与运算符，用于连接多个条件                                                                                 |
| `ANY`                  | 量化比较：表示“大于/小于/等于**任意一个**子查询结果”                                                   |
| `AS`                   | 为表、视图或列指定别名（可省略）                                                                               |
| `ASC`                  | 升序排列（`ORDER BY` 默认）                                                                                  |
| `ASSERTION`            | 定义断言（数据库级完整性约束，可跨表）                                                                         |
| `AUDIT`                | 开启审计功能，将用户操作记录到审计日志                                                                         |
| `AUTHORIZATION`        | 指定模式的所有者（与 `CREATE SCHEMA` 配合）                                                                  |
| `AVG`                  | 求平均值（聚集函数，忽略空值）                                                                                 |
| `BEFORE`               | 触发器时机：在触发事件**之前**执行动作体                                                                 |
| `BEGIN`                | 触发器动作体开始，与 `END` 配合包裹多条 SQL 语句                                                             |
| `BETWEEN`              | 范围谓词：判断值是否在闭区间内（含边界）                                                                       |
| `BIGINT`               | 大整数数据类型（8 字节）                                                                                       |
| `BLOB`                 | 二进制大对象数据类型                                                                                           |
| `BOOLEAN`              | 逻辑布尔数据类型（`TRUE` / `FALSE`）                                                                       |
| `BY`                   | ①`GROUP BY` 分组<br />② `ORDER BY` 排序<br />③ 审计中按会话/访问（`BY SESSION` / `BY ACCESS`）      |
| `CASCADE`              | 级联操作：删除模式/表/视图时一并删除依赖对象；收权时级联收回转授的权限                                         |
| `CASE`                 | 条件表达式（在 `SELECT` 中实现 if-then-else 逻辑）                                                           |
| `CHAR` / `CHARACTER` | 定长字符串数据类型（参数 n 表示长度）                                                                          |
| `CHECK`                | 约束：限制列或表的取值必须满足条件表达式                                                                       |
| `CLOB`                 | 字符串大对象数据类型                                                                                           |
| `CLUSTER`              | 创建聚簇索引（索引顺序与表物理存储顺序一致，一个表最多一个）                                                   |
| `COLUMN`               | `ALTER TABLE` 中指明操作对象为列（可省略）                                                                   |
| `COMMIT`               | 提交事务（笔记仅提及触发器内不能使用）                                                                         |
| `CONSTRAINT`           | 为完整性约束命名                                                                                               |
| `COUNT`                | 统计行数（`COUNT(*)` 包括空值，`COUNT(列)` 忽略空值）                                                      |
| `CREATE`               | 创建数据库对象（模式、表、视图、索引、断言、触发器、角色）                                                     |
| `CREATE ASSERTION`     | 创建断言（全局约束）                                                                                           |
| `CREATE INDEX`         | 创建索引                                                                                                       |
| `CREATE ROLE`          | 创建数据库角色（权限集合）                                                                                     |
| `CREATE SCHEMA`        | 创建模式（命名空间）                                                                                           |
| `CREATE TABLE`         | 创建基本表                                                                                                     |
| `CREATE TRIGGER`       | 创建触发器                                                                                                     |
| `CREATE VIEW`          | 创建视图                                                                                                       |
| `CROSS`                | 交叉连接（`CROSS JOIN` 产生笛卡尔积）                                                                        |
| `DATE`                 | 日期数据类型（`YYYY-MM-DD`）                                                                                 |
| `DECIMAL` / `DEC`    | 定点数数据类型（同 `NUMERIC`）                                                                               |
| `DEFAULT`              | 默认值约束：插入时若未指定该列值，则填入默认值                                                                 |
| `DELETE`               | ① 数据操纵：删除表中的行；② 触发事件：删除操作                                                               |
| `DESC`                 | 降序排列（`ORDER BY` 中使用）                                                                                |
| `DISTINCT`             | 去重：结果集中完全相同的行只保留一行                                                                           |
| `DOUBLE PRECISION`     | 双精度浮点数数据类型（依赖机器精度）                                                                           |
| `DROP`                 | 删除数据库对象（模式、表、视图、索引、断言、触发器）                                                           |
| `DROP ASSERTION`       | 删除断言                                                                                                       |
| `DROP INDEX`           | 删除索引                                                                                                       |
| `DROP SCHEMA`          | 删除模式                                                                                                       |
| `DROP TABLE`           | 删除表（及依赖对象）                                                                                           |
| `DROP TRIGGER`         | 删除触发器                                                                                                     |
| `DROP VIEW`            | 删除视图                                                                                                       |
| `ELSE`                 | `CASE` 表达式中的否则分支                                                                                    |
| `END`                  | 标识触发器动作体结束（与 `BEGIN` 配对）                                                                      |
| `ESCAPE`               | `LIKE` 中指定转义字符（用于匹配 `%` 或 `_` 字面值）                                                      |
| `EXCEPT`               | 集合差运算（返回出现在第一个查询但不在第二个查询中的行）                                                       |
| `EXISTS`               | 存在性子查询：子查询有结果返回真，否则假                                                                       |
| `FLOAT`                | 可选精度浮点数数据类型（精度至少 n 位）                                                                        |
| `FOR EACH ROW`         | 行级触发器：每影响一行触发一次                                                                                 |
| `FOR EACH STATEMENT`   | 语句级触发器：整个 SQL 语句只触发一次（默认）                                                                  |
| `FOREIGN KEY`          | 外键约束：参照另一表的主键或唯一列                                                                             |
| `FROM`                 | 指定查询的数据源（表、视图、派生表）                                                                           |
| `FULL`                 | 全外连接（`FULL OUTER JOIN`）                                                                                |
| `GRANT`                | 授权：为用户或角色分配权限                                                                                     |
| `GROUP BY`             | 按指定列对行进行分组，常与聚集函数配合                                                                         |
| `HAVING`               | 对分组后的结果进行筛选（条件中常用聚集函数）                                                                   |
| `IF`                   | 条件语句（在触发器动作体中使用，笔记未详细展开但提及）                                                         |
| `IN`                   | ① 集合谓词：值是否在列表或子查询结果中；② 连接时指定列名（`INNER JOIN` 可省略 `INNER`）                  |
| `INDEX`                | 索引对象（`CREATE INDEX`、`DROP INDEX`）                                                                   |
| `INNER`                | 内连接（返回两表中满足条件的匹配行）                                                                           |
| `INSERT`               | ① 数据操纵：插入元组<br />② 触发事件：插入操作                                                               |
| `INSTEAD OF`           | 替换型触发器：定义在视图上，代替原始 DML 操作                                                                  |
| `INT` / `INTEGER`    | 长整数数据类型（4 字节）                                                                                       |
| `INTERSECT`            | 集合交运算（返回同时出现在两个查询中的行）                                                                     |
| `INTERVAL`             | 时间间隔数据类型                                                                                               |
| `INTO`                 | ①`INSERT INTO` 指定目标表<br />② `SELECT INTO`（笔记未展开但属 SQL 语法）                                |
| `IS`                   | 与 `NULL` 配合判断空值（`IS NULL` / `IS NOT NULL`）                                                      |
| `JOIN`                 | 连接运算（与 `INNER`、`LEFT` 等合用）                                                                      |
| `LEFT`                 | 左外连接（`LEFT OUTER JOIN`，保留左表所有行）                                                                |
| `LIKE`                 | 字符串模式匹配（`%` 任意长度，`_` 单个字符）                                                               |
| `MAX`                  | 求最大值（聚集函数）                                                                                           |
| `MIN`                  | 求最小值（聚集函数）                                                                                           |
| `NATURAL`              | 自然连接（自动对同名列做等值连接并去重）                                                                       |
| `NEW`                  | 触发器行变量：代表插入后或修改后的新行                                                                         |
| `NOAUDIT`              | 取消审计（关闭指定操作的审计记录）                                                                             |
| `NOT`                  | 逻辑非（用于否定谓词，如 `NOT IN`、`NOT EXISTS`、`NOT NULL`）                                            |
| `NOT NULL`             | 非空约束：该列禁止存储空值                                                                                     |
| `NULL`                 | 空值（与 `IS` 配合使用，不能直接用 `=` 比较）                                                              |
| `NUMERIC`              | 定点数数据类型（`p` 总位数，`d` 小数位数）                                                                 |
| `OFF`                  | 与 `NOAUDIT` 配合（省略，完整为 `NOAUDIT ... OFF` 但笔记未强调）                                           |
| `OLD`                  | 触发器行变量：代表修改前或删除前的旧行                                                                         |
| `ON`                   | ① 外键约束中指定被参照表（`REFERENCES ON DELETE`）<br />② 触发器绑定表<br />③ 连接条件（`ON`）          |
| `ON DELETE`            | 外键违约处理策略（`CASCADE` / `SET NULL` / `NO ACTION`）                                                 |
| `ON UPDATE`            | 外键更新违约处理策略（`CASCADE` / `SET NULL` / `NO ACTION`）                                             |
| `OR`                   | 逻辑或运算符                                                                                                   |
| `ORDER BY`             | 对查询结果进行排序（可多列，指定升/降序）                                                                      |
| `OUTER`                | 外连接（与 `LEFT`、`RIGHT`、`FULL` 配合）                                                                |
| `PRIMARY KEY`          | 主键约束（唯一且非空，一个表只能有一个）                                                                       |
| `PUBLIC`               | 所有用户（授权/收权时的特殊用户组）                                                                            |
| `REAL`                 | 单精度浮点数数据类型（依赖机器精度）                                                                           |
| `REFERENCES`           | 外键约束中指定被参照的表和列                                                                                   |
| `REFERENCING`          | 触发器子句，用于声明 `OLD` / `NEW` 行变量                                                                  |
| `RENAME`               | `ALTER INDEX` 中重命名索引                                                                                   |
| `RESTRICT`             | 限制删除/收权：若存在依赖对象或已转授权限，则拒绝操作                                                          |
| `REVOKE`               | 收回权限（从用户或角色）                                                                                       |
| `RIGHT`                | 右外连接（`RIGHT OUTER JOIN`，保留右表所有行）                                                               |
| `ROLLBACK`             | 回滚事务（笔记仅提及触发器内不能使用）                                                                         |
| `ROLE`                 | 角色（一组权限的集合）                                                                                         |
| `ROW`                  | 触发器行变量类型（`OLD ROW` / `NEW ROW`）                                                                  |
| `SCHEMA`               | 模式（数据库对象的命名容器）                                                                                   |
| `SELECT`               | 数据查询：从表或视图中检索数据                                                                                 |
| `SESSION`              | 审计粒度：按会话记录（`BY SESSION`）                                                                         |
| `SET`                  | ①`UPDATE` 中指定要修改的列及新值<br />② 外键策略 `SET NULL`                                              |
| `SET NULL`             | 外键违约时，将参照列设置为空值                                                                                 |
| `SMALLINT`             | 短整数数据类型（2 字节）                                                                                       |
| `SUM`                  | 求和（聚集函数，忽略空值）                                                                                     |
| `TABLE`                | 基本表对象（`CREATE TABLE`、`DROP TABLE`、`ALTER TABLE`）                                                |
| `THEN`                 | `CASE` 表达式中的结果部分                                                                                    |
| `TIME`                 | 时间数据类型（`HH:MM:SS`）                                                                                   |
| `TIMESTAMP`            | 时间戳数据类型（日期 + 时间）                                                                                  |
| `TO`                   | 授权目标（`GRANT ... TO`）                                                                                   |
| `TRIGGER`              | 触发器对象（`CREATE TRIGGER`、`DROP TRIGGER`）                                                             |
| `UNION`                | 集合并运算（默认去重，`UNION ALL` 保留重复）                                                                 |
| `UNIQUE`               | 唯一约束：列或列组合的值不能重复（允许一个空值）                                                               |
| `UPDATE`               | ① 数据操纵：修改表中数据<br />② 触发事件：修改操作<br />③ 外键 `ON UPDATE` 策略                           |
| `VALUES`               | `INSERT` 语句中提供要插入的具体值                                                                            |
| `VARCHAR`              | 变长字符串数据类型（最大长度 n）                                                                               |
| `VIEW`                 | 视图对象（虚拟表）                                                                                             |
| `WHEN`                 | ①`CASE` 中的条件分支<br />② 触发器中的触发条件（`WHEN` 子句）                                            |
| `WHENEVER`             | 审计子句：`WHENEVER SUCCESSFUL` / `WHENEVER NOT SUCCESSFUL` 指定审计成功或失败的操作                       |
| `WHERE`                | 条件筛选（在查询、更新、删除中限定操作的行）                                                                   |
| `WITH`                 | ① 公用表表达式（`WITH CTE AS`）<br />② `WITH CHECK OPTION`（视图约束）；③ `WITH GRANT OPTION`（授权） |
| `WITH CHECK OPTION`    | 视图约束：通过视图进行的增删改必须满足视图定义条件                                                             |
| `WITH GRANT OPTION`    | 授权选项：被授权者可将获得的权限再授予其他用户                                                                 |

| 类别                                               | 代码示例                                                                                                                                                                                                                                                                                                                                     | 说明                                     |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **模式定义**                                 | `CREATE SCHEMA "S-T" AUTHORIZATION WANG<br>``CREATE TABLE Student (...);`                                                                                                                                                                                                                                                                  | 创建模式并同时建表                       |
| **模式删除**                                 | `DROP SCHEMA "S-T" CASCADE;`                                                                                                                                                                                                                                                                                                               | 级联删除模式及其所有对象                 |
| **建表（列级约束）**                         | ``sql<br>CREATE TABLE Student (<br>    Sno   CHAR(9)   PRIMARY KEY,<br>    Sname CHAR(20)  NOT NULL UNIQUE,<br>    Sage  SMALLINT  CHECK(Sage >= 10 AND Sage <= 30),<br>    Sdept CHAR(20)  DEFAULT 'CS'<br>);<br>``                                                                                                                         | 主键、非空、唯一、检查、默认值           |
| **建表（表级约束）**                         | ``sql<br>CREATE TABLE SC (<br>    Sno    CHAR(9),<br>    Cno    CHAR(4),<br>    Grade  SMALLINT,<br>    PRIMARY KEY (Sno, Cno),<br>    FOREIGN KEY (Sno) REFERENCES Student(Sno) ON DELETE CASCADE,<br>    FOREIGN KEY (Cno) REFERENCES Course(Cno) ON DELETE CASCADE,<br>    CHECK (Grade IS NULL OR (Grade BETWEEN 0 AND 100))<br>);<br>`` | 组合主键、外键级联、表级检查             |
| **约束命名**                                 | `Sage SMALLINT CONSTRAINT CK_Age CHECK(Sage>=10 AND Sage<=30)`                                                                                                                                                                                                                                                                             | 为约束命名                               |
| **修改表（添加列）**                         | `ALTER TABLE Student ADD COLUMN Sbirth DATE;`                                                                                                                                                                                                                                                                                              | 添加新列（示例补充）                     |
| **修改表（删除列）**                         | `ALTER TABLE Student DROP COLUMN Sage CASCADE;`                                                                                                                                                                                                                                                                                            | 删除列，级联删除依赖                     |
| **删除表**                                   | `DROP TABLE Student CASCADE;`                                                                                                                                                                                                                                                                                                              | 删除表及依赖对象                         |
| **创建视图（带检查选项）**                   | ``sql<br>CREATE VIEW IS_Student AS<br>SELECT Sno, Sname, Sage<br>FROM Student<br>WHERE Sdept = 'IS'<br>WITH CHECK OPTION;<br>``                                                                                                                                                                                                              | 信息系学生视图，增删改须满足条件         |
| **删除视图**                                 | `DROP VIEW IS_Student CASCADE;`                                                                                                                                                                                                                                                                                                            | 删除视图，级联删除导出视图               |
| **创建索引**                                 | `CREATE UNIQUE CLUSTER INDEX idx_sno ON Student(Sno ASC);`                                                                                                                                                                                                                                                                                 | 唯一聚簇索引（升序）                     |
| **修改索引（重命名）**                       | `ALTER INDEX idx_sno RENAME TO idx_student_sno;`                                                                                                                                                                                                                                                                                           | 重命名索引                               |
| **删除索引**                                 | `DROP INDEX idx_student_sno;`                                                                                                                                                                                                                                                                                                              | 删除索引                                 |
| **创建断言**                                 | ``sql<br>CREATE ASSERTION ASSE_SC_CNUM<br>CHECK (<br>    10 >= ALL (<br>        SELECT COUNT(*) FROM SC GROUP BY Sno<br>    )<br>);<br>``                                                                                                                                                                                                    | 限制每名学生选课不超过10门               |
| **删除断言**                                 | `DROP ASSERTION ASSE_SC_CNUM;`                                                                                                                                                                                                                                                                                                             | 删除断言                                 |
| **创建触发器（AFTER行级）**                  | ``sql<br>CREATE TRIGGER Student_Count<br>AFTER INSERT ON Student<br>FOR EACH ROW<br>AS<br>BEGIN<br>    UPDATE Dept_Count SET Total = Total + 1;<br>END;<br>``                                                                                                                                                                                | 插入学生后，将对应系人数加1              |
| **创建触发器<br />（BEFORE行级，WHEN条件）** | ``sql<br>CREATE TRIGGER Grade_Check<br>BEFORE UPDATE OF Grade ON SC<br>FOR EACH ROW<br>WHEN (NEW.Grade > 100)<br>AS<br>BEGIN<br>    SET NEW.Grade = 100;<br>END;<br>``                                                                                                                                                                       | 成绩超过100时自动修正为100               |
| **删除触发器**                               | `DROP TRIGGER Grade_Check ON SC;`                                                                                                                                                                                                                                                                                                          | 删除触发器                               |
| **单表查询**                                 | `SELECT Sname, 2023-Sage AS Birth FROM Student;`                                                                                                                                                                                                                                                                                           | 投影、算术表达式、别名                   |
| **去重查询**                                 | `SELECT DISTINCT Sdept FROM Student;`                                                                                                                                                                                                                                                                                                      | 消除重复行                               |
| **带WHERE的查询**                            | `SELECT * FROM Student WHERE Sage < 20;`                                                                                                                                                                                                                                                                                                   | 比较条件                                 |
| **范围查询**                                 | `SELECT * FROM Student WHERE Sage BETWEEN 18 AND 22;`                                                                                                                                                                                                                                                                                      | BETWEEN … AND …                        |
| **集合查询**                                 | `SELECT * FROM Student WHERE Sdept IN ('CS','IS');`                                                                                                                                                                                                                                                                                        | IN 谓词                                  |
| **字符串匹配**                               | `SELECT * FROM Student WHERE Sname LIKE '王_';`                                                                                                                                                                                                                                                                                            | LIKE 通配符（_ 表示单字符）              |
| **空值查询**                                 | `SELECT * FROM SC WHERE Grade IS NULL;`                                                                                                                                                                                                                                                                                                    | IS NULL                                  |
| **EXISTS子查询**                             | ``sql<br>SELECT Sname FROM Student<br>WHERE EXISTS (<br>    SELECT * FROM SC WHERE Sno = Student.Sno AND Cno = '1'<br>);<br>``                                                                                                                                                                                                               | 选修了1号课程的学生                      |
| **分组统计**                                 | ``sql<br>SELECT Sdept, COUNT(*) AS 人数<br>FROM Student<br>GROUP BY Sdept;<br>``                                                                                                                                                                                                                                                             | GROUP BY 与聚集函数                      |
| **分组后筛选**                               | ``sql<br>SELECT Sno, COUNT(*) AS cnt<br>FROM SC<br>GROUP BY Sno<br>HAVING COUNT(*) > 3;<br>``                                                                                                                                                                                                                                                | HAVING 过滤分组                          |
| **排序**                                     | `SELECT * FROM Student ORDER BY Sage DESC, Sno ASC;`                                                                                                                                                                                                                                                                                       | ORDER BY 降序/升序                       |
| **自身连接（隐式）**                         | ``sql<br>SELECT FIRST.Cno, SECOND.Cpno<br>FROM Course FIRST, Course SECOND<br>WHERE FIRST.Cpno = SECOND.Cno;<br>``                                                                                                                                                                                                                           | 查询间接先修课                           |
| **内连接（显式）**                           | `SELECT Sname, Cno FROM Student INNER JOIN SC ON Student.Sno = SC.Sno;`                                                                                                                                                                                                                                                                    | INNER JOIN                               |
| **左外连接**                                 | `SELECT Student.*, Cno FROM Student LEFT JOIN SC ON Student.Sno = SC.Sno;`                                                                                                                                                                                                                                                                 | LEFT OUTER JOIN，保留左表所有行          |
| **派生表查询**                               | ``sql<br>SELECT Sno, avgGrade<br>FROM (SELECT Sno, AVG(Grade) AS avgGrade FROM SC GROUP BY Sno) AS T<br>WHERE avgGrade > 85;<br>``                                                                                                                                                                                                           | FROM 子句中的子查询（派生表）            |
| **相关子查询<br />（NOT EXISTS双重否定）**   | ``sql<br>SELECT Sname FROM Student S<br>WHERE NOT EXISTS (<br>    SELECT * FROM Course C<br>    WHERE NOT EXISTS (<br>        SELECT * FROM SC<br>        WHERE Sno = S.Sno AND Cno = C.Cno<br>    )<br>);<br>``                                                                                                                             | 选修了全部课程的学生                     |
| **集合运算（UNION）**                        | `SELECT Sno FROM Student UNION SELECT Sno FROM Teacher;`                                                                                                                                                                                                                                                                                   | 并集（去重）                             |
| **集合运算（INTERSECT）**                    | `SELECT Sno FROM Student INTERSECT SELECT Sno FROM SC;`                                                                                                                                                                                                                                                                                    | 交集（有选课记录的学生）                 |
| **集合运算（EXCEPT）**                       | `SELECT Sno FROM Student EXCEPT SELECT Sno FROM SC;`                                                                                                                                                                                                                                                                                       | 差集（未选课的学生）                     |
| **WITH子句（CTE）**                          | ``sql<br>WITH DeptAvg AS (<br>    SELECT Sdept, AVG(Sage) AS avgAge FROM Student GROUP BY Sdept<br>)<br>SELECT * FROM DeptAvg WHERE avgAge > 20;<br>``                                                                                                                                                                                       | 公用表表达式（示例补充）                 |
| **插入完整元组**                             | `INSERT INTO Student VALUES ('201215128', '陈冬', 18, 'CS');`                                                                                                                                                                                                                                                                              | 省略列清单，需按表定义顺序提供所有值     |
| **插入部分列**                               | `INSERT INTO Student (Sno, Sname) VALUES ('201215129', '张立');`                                                                                                                                                                                                                                                                           | 指定列，未指定列取默认值或NULL           |
| **插入子查询结果**                           | ``sql<br>INSERT INTO IS_Student (Sno, Sname)<br>SELECT Sno, Sname FROM Student WHERE Sdept = 'IS';<br>``                                                                                                                                                                                                                                     | 批量插入                                 |
| **通过视图插入**                             | ``sql<br>CREATE VIEW IS_Student AS<br>SELECT Sno, Sname, Sage FROM Student WHERE Sdept = 'IS';<br>INSERT INTO IS_Student VALUES ('201215130', '李楠', 19);<br>``                                                                                                                                                                             | 对可更新视图插入，底层表自动填补未显式列 |
| **更新数据**                                 | `UPDATE Student SET Sage = 20 WHERE Sno = '201215128';`                                                                                                                                                                                                                                                                                    | UPDATE … SET … WHERE                   |
| **删除数据**                                 | `DELETE FROM Student WHERE Sno = '201215129';`                                                                                                                                                                                                                                                                                             | DELETE … WHERE                          |
| **授权（基本权限）**                         | `GRANT SELECT ON TABLE Student TO U1;`                                                                                                                                                                                                                                                                                                     | 将查询权限授予单个用户                   |
| **授权（多对象多用户）**                     | `GRANT ALL PRIVILEGES ON TABLE Student, Course TO U2, U3;`                                                                                                                                                                                                                                                                                 | 授予全部权限给多个用户                   |
| **授权（列级权限）**                         | `GRANT SELECT, UPDATE(Grade) ON TABLE SC TO PUBLIC;`                                                                                                                                                                                                                                                                                       | 授予所有用户查询和修改Grade列的权限      |
| **授权（转授权限）**                         | `GRANT SELECT ON TABLE Student TO U4 WITH GRANT OPTION;`                                                                                                                                                                                                                                                                                   | 允许U4再将此权限授予他人                 |
| **收权（级联）**                             | `REVOKE SELECT ON TABLE Student FROM U4 CASCADE;`                                                                                                                                                                                                                                                                                          | 收回U4权限，同时级联收回其转授的权限     |
| **角色操作**                                 | ``sql<br>CREATE ROLE R1;<br>GRANT SELECT ON TABLE Student TO ROLE R1;<br>GRANT R1 TO U1, U2;<br>``                                                                                                                                                                                                                                           | 创建角色、授权角色、将角色授予用户       |
| **开启审计**                                 | `AUDIT SELECT ON Student BY ACCESS WHENEVER SUCCESSFUL;`                                                                                                                                                                                                                                                                                   | 审计对Student表的每一次成功查询          |
| **关闭审计**                                 | `NOAUDIT SELECT ON Student;`                                                                                                                                                                                                                                                                                                               | 取消对Student表SELECT操作的审计          |

### 数据类型

| 数据类型                                 | 含义                                                                        |
| ---------------------------------------- | --------------------------------------------------------------------------- |
| *`CHAR(n)`, `CHARACTER(n)`           | 长度为*n* 的定长字符串                                                    |
| *`VARCHAR(n)`, `CHARACTERVARYING(n)` | 最大长度为*n* 的变长字符串                                                |
| `CLOB`                                 | 字符串大对象                                                                |
| `BLOB`                                 | 二进制大对象                                                                |
| *`INT`, `INTEGER`                    | 长整数（4 字节）                                                            |
| `SMALLINT`                             | 短整数（2 字节）                                                            |
| `BIGINT`                               | 大整数（8 字节）                                                            |
| *`NUMERIC(p, d)`                       | 定点数，由*p* 位数字（不包括符号、小数点）组成，小数点后面有 *d* 位数字 |
| `DECIMAL(p, d)`, `DEC(p, d)`         | 同 `NUMERIC`                                                              |
| `REAL`                                 | 取决于机器精度的单精度浮点数                                                |
| `DOUBLE PRECISION`                     | 取决于机器精度的双精度浮点数                                                |
| *`FLOAT(n)`                            | 可选精度的浮点数，精度至少为*n* 位数字                                    |
| *`BOOLEAN`                             | 逻辑布尔量                                                                  |
| *`DATE`                                | 日期，包含年、月、日，格式为 `YYYY-MM-DD`                                 |
| *`TIME`                                | 时间，包含一日的时、分、秒，格式为 `HH:MM:SS`                             |
| `TIMESTAMP`                            | 时间戳类型                                                                  |
| `INTERVAL`                             | 时间间隔类型                                                                |

### 表达式

用与或非连接谓词，优先级为 `NOT` > `AND` > `OR`。

### 谓词

| 谓词类别 | 语法                                                   | 说明                                                      |
| -------- | ------------------------------------------------------ | --------------------------------------------------------- |
| 比较     | `<表达式> <比较运算符> { <表达式> \| <标量子查询> }`  | 运算符：`=, >, <, >=, <=, <> (或 !=)`                   |
| 范围     | `<表达式> [NOT] BETWEEN <下界> AND <上界>`           | 等价于 `>= 下界 AND <= 上界`                            |
| 集合     | `<表达式> [NOT] IN ( <值列表> \| <子查询> )`          | 值列表用逗号分隔，子查询返回一列                          |
| 字符匹配 | `<列名> [NOT] LIKE '<匹配串>' [ESCAPE '<转义字符>']` | 通配符：`%` 任意长度，`_` 单个字符，`ESCAPE` 转义符 |
| 空值     | `<表达式> IS [NOT] NULL`                             | 不能写成 `= NULL` 或 `!= NULL`                        |
| 存在性   | `[NOT] EXISTS ( <子查询> )`                          | 子查询有结果即为真，通常与相关子查询配合                  |
| 量化比较 | `<表达式> <比较运算符> { ANY \| ALL } ( <子查询> )`   | `> ANY` 大于某个值；`> ALL` 大于所有值                |

* `WHERE` 中 **不能直接使用聚集函数** （如 `WHERE AVG(Grade) > 80` 是错误的）。
* 连接条件也是放在 `WHERE` 中的，例如 `WHERE Student.Sno = SC.Sno`。

### 聚集函数

| 函数                      | 参数       | 说明                                        |
| ------------------------- | ---------- | ------------------------------------------- |
| `COUNT(*)`              | 无         | 统计总行数，不忽略空值                      |
| `COUNT([DISTINCT] col)` | 列名       | 统计该列非空值个数，`DISTINCT` 不重复计数 |
| `SUM([DISTINCT] col)`   | 数值列     | 求和（忽略NULL）                            |
| `AVG([DISTINCT] col)`   | 数值列     | 平均值（忽略NULL）                          |
| `MAX([DISTINCT] col)`   | 任意可比列 | 最大值                                      |
| `MIN([DISTINCT] col)`   | 任意可比列 | 最小值                                      |

> 聚集函数**不能出现在 WHERE**中，只能出现在 SELECT、HAVING 以及 ORDER BY 中。

### 数据定义（CREATE DROP ALTER）

| 操作对象 | 创建             | 删除           | 修改        |
| :------: | ---------------- | -------------- | ----------- |
|   模式   | CREATE SCHEMA    | DROP SCHEMA    |             |
|    表    | CREATE TABLE     | DROP TABLE    | ALTER TABLE |
|   视图   | CREATE VIEW      | DROP VIEW      |             |
|   索引   | CREATE INDEX     | DROP INDEX     | ALTER INDEX |
|   断言   | CREATE ASSERTION | DROP ASSERTION |             |
|  触发器  | CREATE TRIGGER   | DROP TRIGGER   |             |

#### 模式（SCHEMA）

##### 定义模式

```pgsql
CREATE SCHEMA <模式名> AUTHORIZATION <用户名> 
[ <表定义子句> | <视图定义子句> | <授权定义子句> ];
```

```pgsql
CREATE SCHEMA "S-T" AUTHORIZATION WANG
CREATE TABLE Student
    ( Sno   CHAR(9) PRIMARY KEY,
      Sname CHAR(20),
      Sage  SMALLINT,
      Sdept CHAR(20)
    );
```

##### 删除模式

```pgsql
DROP SCHEMA <模式名> { CASCADE | RESTRICT };
```

* **CASCADE** （级联）：删除模式的同时，把该模式中所有数据库对象全部删除。
* **RESTRICT** （限制）：（默认）仅当该模式下没有任何下属对象时才能删除。

```pgsql
DROP SCHEMA "S-T" CASCADE;
```

#### 基本表（TABLE）

##### 定义基本表

```pgsql
CREATE TABLE <表名>
    ( <列名> <数据类型> [ <列级完整性约束> ]
      [, <列名> <数据类型> [ <列级完整性约束> ] ] 
	...
      [, <表级完整性约束> ]
    );
```

###### 列级完整性约束

| 约束类型             | 关键字                                  | 说明                                                                                 | 语法示例                                       |
| -------------------- | --------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------- |
| **非空约束**   | `NOT NULL`<br />（默认可空 `NULL`） | 该列的值不能为空（NULL）。                                                           | `Sname CHAR(20) NOT NULL`                    |
| **唯一约束**   | `UNIQUE`                              | 该列的值必须互不重复，允许一个空值。                                                 | `Sname CHAR(20) UNIQUE`                      |
| **主码约束**   | `PRIMARY KEY`                         | 该列是主键，自动包含 `NOT NULL` 和 `UNIQUE`。 **只适用于单列主码** 。      | `Sno CHAR(9) PRIMARY KEY`                    |
| **检查约束**   | `CHECK(<条件>)`                       | 该列的取值必须满足布尔表达式。                                                       | `Sage SMALLINT CHECK(Sage>=10 AND Sage<=30)` |
| **默认值约束** | `DEFAULT <值>`                        | 插入元组时若未提供该列值，则自动填入默认值。                                         | `Sdept CHAR(20) DEFAULT 'CS'`                |
| **外码约束**   | `REFERENCES <父表>(<列>)`             | 定义该列为外键，参照指定关系的指定列。<br />要求父表对应列必须是主键或具有唯一约束。 | `Sno CHAR(9) REFERENCES Student(Sno)`        |

```pgsql
CREATE TABLE Student (
    Sno   CHAR(9)   PRIMARY KEY,         -- 主码
    Sname CHAR(20)  NOT NULL UNIQUE,     -- 非空且唯一
    Sage  SMALLINT  CHECK(Sage >= 10 AND Sage <= 30),  -- 取值约束
    Sdept CHAR(20)  DEFAULT 'CS'         -- 默认值
);
```

###### 表级完整性约束

| 约束类型           | 关键字                                                                                  | 说明                                                                                                           | 语法示例                                                        |
| ------------------ | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **主码约束** | `PRIMARY KEY (列1, 列2, ...)`                                                         | 定义组合主键，<br />适用于多列联合作为主码的情况。                                                             | `PRIMARY KEY (Sno, Cno)`                                      |
| **唯一约束** | `UNIQUE (列1, 列2, ...)`                                                              | 定义组合唯一约束，<br />多个列的值组合不允许重复。                                                             | `UNIQUE (Sname, Sdept)`                                       |
| **外码约束** | `FOREIGN KEY (列) REFERENCES 父表(列)`<br />`[ON DELETE <策略>] [ON UPDATE <策略>]` | 定义外键，并可指定<br />当被参照表被删除<br />或更新时的违约处理策略<br />（CASCADE / SET NULL / NO ACTION）。 | `FOREIGN KEY (Sno) REFERENCES Student(Sno) ON DELETE CASCADE` |
| **检查约束** | `CHECK (<条件>)`                                                                      | 定义涉及多个列或更复杂的检查条件。                                                                             | `CHECK (Grade IS NULL OR (Grade>=0 AND Grade<=100))`          |

```pgsql
CREATE TABLE SC (
    Sno    CHAR(9),
    Cno    CHAR(4),
    Grade  SMALLINT,
    -- 表级主码
    PRIMARY KEY (Sno, Cno),
    -- 表级外码，并指定级联删除
    FOREIGN KEY (Sno) REFERENCES Student(Sno) ON DELETE CASCADE,
    FOREIGN KEY (Cno) REFERENCES Course(Cno) ON DELETE CASCADE,
    -- 表级检查约束
    CHECK (Grade IS NULL OR (Grade BETWEEN 0 AND 100))
);
```

###### 约束命名

```pgsql
CONSTRAINT <约束名> <约束定义>
```

```pgsql
Sage SMALLINT CONSTRAINT CK_Age CHECK(Sage>=10 AND Sage<=30)
```

```pgsql
CONSTRAINT PK_SC PRIMARY KEY (Sno, Cno)
```

###### 约束违约处理

* 拒绝执行
* 级联操作
* 设置为空值

| 被参照表（例如 Student） | 参照表（例如 SC） | 违约处理                 |
| :----------------------- | :---------------- | :----------------------- |
|                          | 插入元组          | 拒绝                     |
|                          | 修改外码值        | 拒绝                     |
| 删除元组                 |                   | 拒绝/级联删除/设置为空值 |
| 修改主码值               |                   | 拒绝/级联修改/设置为空值 |

##### 修改基本表（ALTER）

```pgsql
ALTER TABLE <表名>
    [ ADD [COLUMN] <新列名> <数据类型> [ <完整性约束> ] ]   /* 新增列或表级约束 */
    [ ADD <表级完整性约束> ]                              /* 新增表级约束 */
    [ DROP [COLUMN] <列名> [ CASCADE | RESTRICT ] ]       /* 删除列 */
    [ DROP CONSTRAINT <约束名> [ RESTRICT | CASCADE ] ]   /* 删除约束 */
    [ ALTER COLUMN <列名> <数据类型> ];                    /* 修改列的数据类型 */
```

```sql
ALTER TABLE Student DROP COLUMN Sage CASCADE;
```

##### 删除基本表（DROP）

```sql
DROP TABLE <表名> [ RESTRICT | CASCADE ];
```

* `RESTRICT`：若该表被其他对象引用（如视图、外键），则不允许删除。
* `CASCADE`：删除表的同时，与之相关的依赖对象（视图、外键等）也一同删除。

#### 视图（VIEW）

##### 定义视图

```pgsql
CREATE VIEW <视图名> [ ( <列名> [ ,...n ] ) ]
AS <子查询或视图>
[ WITH CHECK OPTION ];
```

* 子查询可以是任意 `SELECT`子句，是否可以含有 `ORDER BY`或 `DISTINCT`看情况。
* `WITH CHECK OPTION`：通过视图进行插入、更新、删除操作时，必须满足视图定义中的条件。

**示例** ：建立信息系学生的视图，并要求对视图的增删改都只局限于信息系学生。

```pgsql
CREATE VIEW IS_Student
AS
SELECT Sno, Sname, Sage
FROM Student
WHERE Sdept = 'IS'
WITH CHECK OPTION;
```

##### 删除视图

```sql
DROP VIEW <视图名> [ CASCADE ];
```

* CASCADE：级联删除由该视图导出的其他视图。
* 默认如果有子视图就拒绝拒绝

##### 更新视图

定义视图时有 `WITH CHECK OPTION`时时，执行更新操作时不满足视图约束条件会拒绝执行。

#### 索引（INDEX）

##### 定义索引

```sql
CREATE [ UNIQUE ] [ CLUSTER ] INDEX <索引名>
ON <表名> ( <列名> [ ASC | DESC ] [ ,...n ] );
```

* **UNIQUE** ：这个索引的每个索引值对应的数据记录是唯一的。
* **CLUSTER** ：聚簇索引，即索引顺序与表记录的物理存储顺序一致（一个表最多一个聚簇索引）。
* 次序：ASC（升序，默认）或 DESC（降序）。

##### 修改索引

只有对索引的重命名操作

```pgsql
ALTER INDEX <旧索引名> RENAME TO <新索引名>
```

##### 删除索引

```pgsql
DROP INDEX <索引名>;
```

#### 断言（ASSERTION）

##### 定义断言

断言是一种**数据库级的完整性约束**，可以定义涉及**多个表**或**复杂逻辑**的约束条件，比列级和表级约束更强大。当任何相关表的数据发生变化时，系统会自动检查断言，若违反则拒绝操作。

```pgsql
CREATE ASSERTION <断言名>
CHECK ( <条件表达式> );
```

- 条件表达式可以是任意返回布尔值的 SQL 表达式，通常包含子查询、聚集函数等。
- 断言独立于表，作用于整个数据库，创建时不会绑定到特定表。

##### 删除断言

```pgsql
DROP ASSERTION <断言名>;
```

##### 示例

1. **限制学生的选课数量不能超过 10 门**

   ```pgsql
   CREATE ASSERTION ASSE_SC_CNUM
   CHECK (
       10 >= ALL (
           SELECT COUNT(*) 
           FROM SC 
           GROUP BY Sno
       )
   );
   ```

   当向 `SC` 表插入或修改记录时，若任一学生的选课总数超过 10，系统拒绝该操作。
2. **限制每门课的选修人数不超过教室容量**

   假设 `Course` 表有 `Cno` 和 `Capacity` 两列，则：

   ```pgsql
   CREATE ASSERTION ASSE_SC_CAP
   CHECK (
       NOT EXISTS (
           SELECT Cno 
           FROM SC 
           GROUP BY Cno 
           HAVING COUNT(*) > (
               SELECT Capacity 
               FROM Course 
               WHERE Course.Cno = SC.Cno
           )
       )
   );
   ```

   任何可能导致某门课选课人数超过其容量的插入或修改都会被拒绝。

##### 断言与 CHECK 约束的区别

| 对比项             | 断言（ASSERTION）                | CHECK 约束                   |
| ------------------ | -------------------------------- | ---------------------------- |
| **作用范围** | 整个数据库，可跨多表             | 单个列或多个列（表级）       |
| **复杂度**   | 支持子查询、聚集函数等复杂条件   | 不能引用其他表的列           |
| **定义位置** | 独立于表定义                     | 在列级或表级完整性约束中定义 |
| **使用场景** | 需要跨表或全局条件的复杂业务规则 | 单表内一行的取值限制         |

#### 触发器（TRIGGER）

```pgsql
CREATE TRIGGER <触发器名>
{ BEFORE | AFTER } <触发事件>
 ON <表名>
[ REFERENCING { OLD | NEW } ROW AS <变量名> ]
[ FOR EACH { ROW | STATEMENT } ]
[ WHEN <触发条件> ]
<触发动作体>;
```

| 成分                             | 说明                                                                             |
| -------------------------------- | -------------------------------------------------------------------------------- |
| **`CREATE TRIGGER`**     | 创建触发器                                                                       |
| **`<触发器名>`**         | 触发器的名称                                                                     |
| **`BEFORE`**             | 在触发事件**之前**激活触发器。通常用于检查数据合法性、设置初始值等         |
| **`AFTER`**              | 在触发事件**之后**激活触发器。通常用于记录日志、级联更新等                 |
| **`<触发事件>`**         | 可以是 `INSERT`, `DELETE`, `UPDATE`，或它们的组合                          |
| **`ON <表名>`**          | 触发器只能定义在**基本表**上，不能定义在视图上                             |
| **`REFERENCING...`**     | 定义行变量：`OLD ROW` 表示修改/删除前的旧行；`NEW ROW` 表示插入/修改后的新行 |
| **`FOR EACH ROW`**       | 行级触发器：SQL语句每影响一行，就触发一次                                        |
| **`FOR EACH STATEMENT`** | 语句级触发器：无论SQL语句影响多少行，只触发一次（默认）                          |
| **`[WHEN <触发条件>]`**  | 触发条件，只有满足条件时才执行触发动作体                                         |
| **`<触发动作体>`**       | 触发时要执行的SQL语句或存储过程。若有多条语句，需用 `BEGIN...END`包裹          |

##### 触发时机（BEFORE AFTER INSTEAD OF）

```pgsql
{ BEFORE | AFTER } <触发事件> ON <表名>
```

| 时机                 | 说明                                                       | 使用场景                                                      |
| -------------------- | ---------------------------------------------------------- | ------------------------------------------------------------- |
| **BEFORE**     | 在触发事件执行**之前**激活。                         | 数据校验、修正即将写入的值、设置默认值。                      |
| **AFTER**      | 在触发事件执行**之后**激活。                         | 审计日志、级联更新其他表、发送通知。                          |
| **INSTEAD OF** | **替换**触发事件的操作，必须定义在**视图**上。 | 将视图的 DML 操作转换为对基本表的操作，实现复杂的可更新视图。 |

* `BEFORE` 触发器不能包含修改数据库的操作（某些 DBMS），一般只做数据校验和变量设置。
* `AFTER` 触发器可以执行完整的数据修改。
* `INSTEAD OF` 必须定义在视图上，且每个事件只能定义一个。

##### 触发事件

```pgsql
{ INSERT | DELETE | UPDATE [ OF <列名> [ , ... ] ] }
    [ OR { INSERT | DELETE | UPDATE } ... ]
```

* 触发事件可以是单个，也可以用 `OR` 连接多个事件。
* **INSERT** ：向表中插入新行时触发。
* **DELETE** ：从表中删除行时触发。
* **UPDATE** ：修改表中已有行时触发。可以用 `OF <列名>` 指定**仅当某（些）列被修改**时才触发，不指定则任意列被修改都触发。

##### ON子句

```pgsql
ON <表名>
```

* 触发器必须绑定到一个 **基本表** （除 INSTEAD OF 外）。
* 不能直接在视图上定义 BEFORE/AFTER 触发器。

##### REFERENCING子句

```pgsql
REFERENCING OLD ROW AS <旧行变量名>
             NEW ROW AS <新行变量名>
```

* 用于声明 **行变量** ，以便在动作体中访问触发事件影响的行数据。
* **OLD ROW** ：代表修改前或删除前的旧行。
* **NEW ROW** ：代表插入后或修改后的新行。
* 该子句仅在 **FOR EACH ROW** 行级触发器中有实际意义。
* 不同事件可用的行变量：

| 事件   | OLD ROW          | NEW ROW          |
| ------ | ---------------- | ---------------- |
| INSERT | ✗               | ✓（新插入的行） |
| DELETE | ✓（被删除的行） | ✗               |
| UPDATE | ✓（修改前的值） | ✓（修改后的值） |

##### FOR EACH ROW / FOR EACH STATEMENT

没写时默认FOR EACH STATEMENT

| 粒度                         | 说明                                                                                    |
| ---------------------------- | --------------------------------------------------------------------------------------- |
| **FOR EACH ROW**       | 行级触发器，SQL 语句每影响**一行**就触发一次，动作体执行次数 = 受影响的行的数量。 |
| **FOR EACH STATEMENT** | 语句级触发器，**默认**选项，无论 SQL 语句影响多少行，只触发一次。                 |

##### 触发动作体

```pgsql
BEGIN
    [<声明部分>]       -- 可选，用于声明变量
    <执行语句列表>     -- 核心，单条或多条SQL语句
END
```

* 可包含：赋值语句、条件语句、循环语句、SQL 操纵语句。
* 可引用 NEW / OLD 行变量。
* **限制** ：不能包含 `COMMIT` 或 `ROLLBACK`。
* 执行失败会导致触发语句回滚。

##### 触发器执行顺序

1. **BEFORE 语句级** 触发器
2. **BEFORE 行级** 触发器（对每一行）
3. **执行触发的 SQL 语句本身** （INSERT/UPDATE/DELETE）
4. **AFTER 行级** 触发器（对每一行）
5. **AFTER 语句级** 触发器

##### 删除触发器

```pgsql
DROP TRIGGER <触发器名> ON <表名>;   -- 某些DBMS需要 ON 子句
-- 或
DROP TRIGGER <触发器名>;
```

```pgsql
-- ① 插入学生记录时，自动将某计数表的学生总数加1
CREATE TRIGGER Student_Count
AFTER INSERT ON Student
FOR EACH ROW
AS
BEGIN
    UPDATE Dept_Count SET Total = Total + 1;
END;

-- ② 修改成绩时，确保新成绩不大于100
CREATE TRIGGER Grade_Check
BEFORE UPDATE OF Grade ON SC
FOR EACH ROW
WHEN (NEW.Grade > 100)
AS
BEGIN
    SET NEW.Grade = 100;
END;
```

### 数据查询（SELECT）

教材版本

```pgsql
SELECT [ALL | DISTINCT] <目标列表达式> [别名] [,<目标列表达式> [别名]] …
FROM <表名或视图名> [别名] [,<表名或视图名> [别名]] … | (<SELECT 语句>) [AS] <别名>
[WHERE <条件表达式>]
[GROUP BY <列名 1> [HAVING <条件表达式>]]
[ORDER BY <列名 2> [ASC | DESC]];
```

AI版本

```pgsql
SELECT [ALL | DISTINCT] <目标列表达式> [[AS] 别名] [, ...]
FROM <表名或视图名> [[AS] 别名] [, ...]
[WHERE <条件表达式>]
[GROUP BY <列名1> [, ...] [HAVING <分组条件>]]
[ORDER BY <列名2> [ASC | DESC] [, ...]];
```

详细版本

```pgsql
[ WITH <公用表表达式> [, ...] ]
SELECT [ ALL | DISTINCT ] <目标列表达式> [ [AS] 别名 ] [, ...]
FROM <表或视图或子查询> [ [AS] 别名 ] [ <连接类型> JOIN <表> ON <条件> ] ...
[ WHERE <条件表达式> ]
[ GROUP BY <列名> [, ...] [ HAVING <分组条件> ] ]
[ ORDER BY <排序列> [ ASC | DESC ] [, ...] ];
```

执行顺序

1. **FROM** ：确定数据来源（表/视图/派生表），做笛卡尔积。
2. **WHERE** ： 对每一行进行条件筛选。
3. **GROUP BY** ：将剩余行按指定列分组。
4. **HAVING** ： 过滤不符合条件的分组（条件中常用聚集函数）。
5. **SELECT** ： 确定最终输出的列或表达式，进行去重（DISTINCT），应用别名。
6. **ORDER BY** ：对最终结果排序。

> `WHERE` 中不能使用聚集函数，聚集函数的筛选必须放在 `HAVING` 中。

#### SELECT子句

##### ALL和DISTINCT

```pgsql
SELECT [ALL | DISTINCT] <目标列表达式> [别名] [,<目标列表达式> [别名]] …
```

* **ALL** ：默认值，返回全部行， **包含完全重复的行** 。
* **DISTINCT** ：消除结果集中完全相同的行，保留唯一组合。

##### 目标列表达式

| 类型               | 说明                                    | 示例                                                  |
| ------------------ | --------------------------------------- | ----------------------------------------------------- |
| 普通列名           | 表中定义的列                            | `Sno`, `Sname`                                    |
| `*`              | **所有列** ，等同于列出表中全部列 | `SELECT * FROM Student;`                            |
| `表名.*`         | 指定表的所有列                          | `SELECT Student.*`                                  |
| 算术表达式         | 列、常量、运算符组成的计算表达式        | `2023 - Sage`，`Grade * 1.2`                      |
| 字符串常量         | 在结果中直接加一列常量字符串            | `'学号:'`, `'出生年份'`                           |
| 函数               | 系统函数，如数学、字符串、日期函数      | `LOWER(Sdept)`                                      |
| **聚集函数** | 对一组值进行计算，配合分组使用          | `COUNT(*)`, `AVG(Grade)`, `MAX(Grade)`          |
| 标量子查询         | 返回单个值的子查询（极少用）            | `(SELECT MAX(Grade) FROM SC)`                       |
| CASE表达式         | 条件判断表达式                          | `CASE WHEN Grade>=60 THEN '及格' ELSE '不及格' END` |

> 注意：当使用了聚集函数且没有 `GROUP BY` 时，整个表当作一组，此时目标列中不能混入普通列名（否则会出错）。有 `GROUP BY` 时，普通列必须是分组列。

##### 别名

跟在目标列表达式后，中间无需 `AS` 关键字（也可加），直接空格加别名。别名用于改变查询结果中的列标题。

```pgsql
-- 示例：计算列、别名、去重
SELECT DISTINCT Sno, 2023-Sage AS Birth, LOWER(Sdept) dept
FROM Student;
```

#### FROM子句

```pgsql
FROM <表名或视图名> [别名] [,<表名或视图名> [别名]] … | (<SELECT 语句>) [AS] <别名>
```

##### 直接引用表或视图

```pgsql
FROM <表名或视图名> [别名] [,<表名或视图名> [别名]] …
```

```pgsql
-- 单表查询
SELECT * FROM Student;
-- 两个表隐式等值连接
SELECT Sname, Cno FROM Student S, SC
WHERE S.Sno = SC.Sno;
-- 自身连接：查询间接先修课
SELECT FIRST.Cno, SECOND.Cpno
FROM Course FIRST, Course SECOND
WHERE FIRST.Cpno = SECOND.Cno;
```

多表连接类型

| 连接类型               | 说明                                   |
| ---------------------- | -------------------------------------- |
| `[INNER] JOIN`       | 内连接，只返回匹配行                   |
| `LEFT [OUTER] JOIN`  | 左外连接，左表所有行保留，无匹配用NULL |
| `RIGHT [OUTER] JOIN` | 右外连接，右表所有行保留               |
| `FULL [OUTER] JOIN`  | 全外连接，左右表所有行保留             |
| `CROSS JOIN`         | 笛卡尔积（无ON条件）                   |
| `NATURAL JOIN`       | 自然连接（自动找同名列等值连接，去重） |

```pgsql
-- 内连接
SELECT Sname, Cno FROM Student INNER JOIN SC ON Student.Sno = SC.Sno;
-- 左外连接（包含未选课学生）
SELECT Student.*, Cno FROM Student LEFT JOIN SC ON Student.Sno = SC.Sno;
```

##### 子查询作为派生表

```pgsql
FROM (<SELECT 语句>) [AS] <别名>
```

```pgsql
-- 查询每个学生的平均成绩，并筛选平均分>85的
SELECT Sno, avgGrade
FROM (SELECT Sno, AVG(Grade) AS avgGrade FROM SC GROUP BY Sno) AS T
WHERE avgGrade > 85;
```

#### WHERE子句

```pgsql
[WHERE <条件表达式>]
```

```pgsql
-- 比较
SELECT * FROM Student WHERE Sage < 20;

-- 范围
SELECT * FROM Student WHERE Sage BETWEEN 18 AND 22;

-- 集合
SELECT * FROM Student WHERE Sdept IN ('CS', 'IS');

-- 字符匹配：姓“王”且全名两字
SELECT * FROM Student WHERE Sname LIKE '王_';

-- 空值
SELECT * FROM SC WHERE Grade IS NULL;

-- EXISTS：查询选修了1号课程的学生姓名
SELECT Sname FROM Student
WHERE EXISTS (
    SELECT * FROM SC WHERE Sno = Student.Sno AND Cno = '1'
);
```

#### GROUP BY 和 HAVING 子句

##### GROUP BY

* 将 `WHERE` 筛选后的行按 `<列名 1>` 的值分组，值相等的为一组。
* 可以按多列分组，用逗号分隔：`GROUP BY 列1, 列2`，分组顺序按先列1再列2。
* 空值视为一个独立分组。

 **作用** ：分组后，聚集函数作用于 **每个分组** ，而非全表。

```pgsql
SELECT Sdept, COUNT(*) AS 人数
FROM Student
GROUP BY Sdept;
```

##### HAVING

* 紧跟在 `GROUP BY` 之后，用于对**分组后的结果**进行筛选。
* 条件中通常包含**聚集函数**或分组列。
* 如果使用了 `HAVING` 而没有 `GROUP BY`，则整张表视作一组（某些DBMS允许，但标准要求有 GROUP BY）。

> **WHERE 与 HAVING 的区别** ：
>
> * `WHERE` 对原始表的**每一行**进行过滤（分组前）。
> * `HAVING` 对 **GROUP BY 产生的组**进行过滤（分组后）。

```pgsql
-- 查询选课超过3门的学生学号及选课数
SELECT Sno, COUNT(*) AS cnt
FROM SC
GROUP BY Sno
HAVING COUNT(*) > 3;

-- 查询平均成绩大于85的课程，且排除选课人数少于5人的课程
SELECT Cno, AVG(Grade) AS avgG
FROM SC
WHERE Grade IS NOT NULL
GROUP BY Cno
HAVING COUNT(*) >= 5 AND AVG(Grade) > 85;
```

* `SELECT` 中出现的**非聚集列**必须出现在 `GROUP BY` 中，否则是语法错误。
* `HAVING` 中可以使用聚集函数，也可以使用分组列，但不能单独使用未出现在 `GROUP BY` 中的列。

#### ORDER BY子句

```pgsql
[ORDER BY <列名 2> [ASC | DESC]]
```

* 对最终查询结果进行排序。
* `<列名 2>` 可以是列名、列别名、计算表达式，甚至是 `SELECT` 列表中列的位置序号（如 `ORDER BY 2 DESC`）。
* `ASC`：升序（默认）；`DESC`：降序。
* 可以按多级排序：`ORDER BY 列1 DESC, 列2 ASC`，先按列1降序，若相同再按列2升序。
* 执行顺序是 **最后一步** ，所以可以使用别名，这是与 `WHERE`/`GROUP BY` 不同的地方。
* **子查询的 SELECT 语句中不能有 ORDER BY** （ORDER BY 只能修饰最外层查询）。
* 空值通常被视为最大值。

```pgsql
SELECT Sno, AVG(Grade) AS avgG
FROM SC
GROUP BY Sno
ORDER BY avgG DESC, Sno ASC;
```

#### 子查询

##### 子查询出现位置

* **WHERE 或 HAVING 中** ：作为比较对象（标量）、集合成员（IN）、存在性测试（EXISTS）、量化比较（ANY/ALL）。
* **FROM 中** ：作为派生表（必须有别名）。
* **SELECT 中** ：作为标量子查询（仅返回单值）。

##### 重要规则

* 子查询的 `SELECT` 语句 **不能使用 `ORDER BY`** （除非有 `LIMIT`，但教材不提，只强调不能有 ORDER BY）。
* 标量子查询必须返回单行单列；若返回多行则运行时出错。
* **相关子查询** ：内查询引用了外查询的表列，外查询每一行都会驱动内查询重新执行。

##### 相关子查询和全称量词

用 `NOT EXISTS` 双重否定表达“所有…”。例如“选修了全部课程的学生”：

```pgsql
SELECT Sname FROM Student S
WHERE NOT EXISTS (
    SELECT * FROM Course C
    WHERE NOT EXISTS (
        SELECT * FROM SC
        WHERE Sno = S.Sno AND Cno = C.Cno
    )
);
```

#### 集合运算

将多个 `SELECT` 语句的结果合并为一个结果集。

```pgsql
<查询语句>
{ UNION [ ALL ] | INTERSECT [ ALL ] | EXCEPT [ ALL ] }
<查询语句>
```

* `UNION`：并集，默认去除重复行；`UNION ALL` 保留所有重复。
* `INTERSECT`：交集。
* `EXCEPT`（或 `MINUS`）：差集。
* 要求：各查询结果的 **列数相同** ， **对应列类型兼容** 。
* `ORDER BY` 只能出现在最后一条语句之后，对整个合并结果排序。

#### WITH子句

```pgsql
WITH <CTE名> [(列列表)] AS ( <查询> )
SELECT ... FROM <CTE名> ...
```

单表查询

连接查询

嵌套查询

集合查询

基于派生表的查询（FROM）

### 数据更新（INSERT UPDATE DELETE）

#### 插入数据（INSERT）

```pgsql
INSERT
INTO <表名 或 可更新视图名> [ ( <属性列1> [, <属性列2> ... ] ) ]
{ VALUES ( <常量1> [, <常量2> ... ] ) | <子查询> };
```

##### INTO子句

```pgsql
INTO <表名或视图名> [ ( <属性列1> [, <属性列2> ... ] ) ]
```

* 可以是基本表名，也可以是可更新视图名
* 如果是 **视图** ：插入操作转换为对底层基本表的插入。视图中未包含的列，在底层表中取默认值或空值（若不允许且无默认值则插入失败）。
* 列的顺序可以与表定义顺序**不一致**，但必须与 VALUES 或子查询一一对应。
* 如果**省略**此括号部分，表示要给表的所有列赋值，此时 VALUES 或子查询必须提供全部列的值，且顺序必须与表定义完全一致。

##### VALUE子句

```pgsql
VALUES ( <常量1> [, <常量2> ... ] );
```

* 只用于插入单个元组。
* 常量与列清单一一对应： **数量必须相等，顺序一一对应，数据类型必须兼容** 。
* 字符型和日期型常量要用单引号括起。

##### 子查询子句

```pgsql
<子查询>
```

* 用于一次插入多个元组，子查询的结果就是要插入的行集。
* 子查询 **不能加 ORDER BY** 。
* 子查询返回的列数、列序及各列数据类型，必须与 INTO 子句中的列清单完全匹配。

##### 值与列的映射规则

| 情况       | 规则                                                                               |
| ---------- | ---------------------------------------------------------------------------------- |
| 省列清单   | VALUES 必须按表定义列顺序提供所有列的值                                            |
| 列出部分列 | 未列出的列自动取默认值（若有定义）或空值（允许NULL时），不允许NULL且无默认值则报错 |
| 值顺序     | 与列清单顺序一一对应（不是表定义序）                                               |

```pgsql
-- ===== 对基本表插入 =====
-- ① 插入完整元组（省略列清单）
INSERT INTO Student VALUES ('201215128', '陈冬', 18, 'CS');

-- ② 插入部分列
INSERT INTO Student (Sno, Sname) VALUES ('201215129', '张立');

-- ③ 插入子查询结果
INSERT INTO IS_Student (Sno, Sname)
SELECT Sno, Sname FROM Student WHERE Sdept = 'IS';


-- ===== 对视图插入 =====
-- 创建信息系学生视图（行列子集视图，可更新）
CREATE VIEW IS_Student AS
SELECT Sno, Sname, Sage
FROM Student
WHERE Sdept = 'IS';

-- 通过视图插入
INSERT INTO IS_Student VALUES ('201215130', '李楠', 19);
-- 实际效果：向 Student 表插入一行，Sdept 自动填 NULL（或默认值）

-- 加上 WITH CHECK OPTION 的视图
CREATE VIEW IS_Student_Check AS
SELECT Sno, Sname, Sage
FROM Student
WHERE Sdept = 'IS'
WITH CHECK OPTION;

-- 通过该视图插入时，必须满足 Sdept = 'IS'
-- 但因视图中无 Sdept 列，插入可能失败，除非底层表 Sdept 有默认值 'IS'
INSERT INTO IS_Student_Check VALUES ('201215131', '王芳', 20);
-- 若 Sdept 无默认值，此操作失败
```

#### 更新数据（UPDATE）

```pgsql
UPDATE <表名或视图名>
SET <列名> = <表达式> [, <列名> = <表达式> ... ]
[ WHERE <条件> ];
```

#### 删除数据（DELETE）

```pgsql
DELETE
FROM <表名 或 可更新视图名>
[ WHERE <条件> ];
```

#### 可更新视图的条件

行列子集视图

| 条件                  | 说明                                                               |
| --------------------- | ------------------------------------------------------------------ |
| **单表导出**    | 视图从**单个基本表**导出                                     |
| **无聚集**      | SELECT 子句不含聚集函数（COUNT, SUM, AVG, MAX, MIN）               |
| **无 DISTINCT** | 没有 `DISTINCT` 关键字                                           |
| **无 GROUP BY** | 没有分组子句                                                       |
| **无计算列**    | 目标列不包含算术表达式或函数计算的结果列（而是直接映射基本表的列） |
| **保留主码**    | 基本表的主码必须出现在视图中（否则基本表无法唯一标识要更新的行）   |

删除全部数据保留表只需用 `DELETE FROM <表名 或 可更新视图名>`

#### WITH CHECK OPTION约束

| 操作             | 约束效果                                                                                |
| ---------------- | --------------------------------------------------------------------------------------- |
| **INSERT** | 新插入的元组必须满足视图定义中的 WHERE 条件                                             |
| **UPDATE** | 修改后的元组必须仍然满足视图定义中的 WHERE 条件（即不能通过 UPDATE 将元组“改出”视图） |
| **DELETE** | 删除本身不会新增/修改数据，故 CHECK 通常不影响，只是确保删除范围限定在视图条件内        |

### 用户管理（）

### 权限管理（GRANT REVOKE）

#### 授权（GRANT）

```pgsql
GRANT <权限列表>
ON <对象类型> <对象名>
TO <用户列表> [ , ... ] | PUBLIC
[ WITH GRANT OPTION ];
```

| 成分                                 | 说明                                                                                                    |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| **`GRANT`**                  | 授权关键字                                                                                              |
| **`<权限列表>`**             | 一个或多个由逗号分隔的权限关键字，如 `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `ALL PRIVILEGES` |
| **`ON <对象类型> <对象名>`** | 指定授权的目标。对象类型可以是 `TABLE`、`VIEW` 等，如 `ON TABLE Student`                          |
| **`TO <用户列表>`**          | 被授权的用户，若为所有用户则用 `PUBLIC`                                                               |
| **`[WITH GRANT OPTION]`**    | 如果指定，则被授权者**有权将其获得的权限再授予其他用户**                                          |

```pgsql
-- ① 把查询 Student 表的权限授予用户 U1
GRANT SELECT ON TABLE Student TO U1;

-- ② 把对 Student 表和 Course 表的全部权限授予用户 U2 和 U3
GRANT ALL PRIVILEGES ON TABLE Student, Course TO U2, U3;

-- ③ 把查询 SC 表和修改成绩的权限授予所有用户
GRANT SELECT, UPDATE(Grade) ON TABLE SC TO PUBLIC;

-- ④ 把查询 Student 表的权限授予 U4，并允许其将此权限再授予他人
GRANT SELECT ON TABLE Student TO U4 WITH GRANT OPTION;
```

#### 收权（REVOKE）

```pgsql
REVOKE <权限列表>
ON <对象类型> <对象名>
FROM <用户列表> [ , ... ] | PUBLIC
[ CASCADE | RESTRICT ];
```

| 成分                               | 说明                                                                                                                                                                                            |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`REVOKE`**               | 收权关键字                                                                                                                                                                                      |
| **`<权限列表>`**           | 与 GRANT 相同                                                                                                                                                                                   |
| **`FROM <用户列表>`**      | 被收回权限的用户                                                                                                                                                                                |
| **`[CASCADE \| RESTRICT]`** | `CASCADE`： **级联收回** ，<br />不仅收回该用户的权限，也收回该用户转授给其他人的该权限；<br />`RESTRICT`： **限制收回** ，<br />如果该用户已将权限转授他人，则拒绝本次收回操作 |

```pgsql
-- ① 收回用户 U1 对 Student 表的查询权限
REVOKE SELECT ON TABLE Student FROM U1;

-- ② 收回所有用户对 SC 表的查询权限
REVOKE SELECT ON TABLE SC FROM PUBLIC;

-- ③ 级联收回 U4 的查询权限
REVOKE SELECT ON TABLE Student FROM U4 CASCADE;
```

#### 数据库角色

角色是 **一组权限的集合** 。使用角色可以简化对多个用户的授权管理。在SQL中首先用 `CREATE ROLE`语句创建角色，然后用 `GRANT`语句给角色授权，用 `REVOKE`语句收回授予角色的权限。

```pgsql
-- ① 创建角色
CREATE ROLE <角色名>;

-- ② 给角色授权
GRANT <权限列表> ON <对象类型> <对象名> TO ROLE <角色名>;

-- ③ 将角色授予用户
GRANT <角色名> TO <用户列表>;

-- ④ 收回角色权限
REVOKE <权限列表> ON <对象类型> <对象名> FROM ROLE <角色名>;
```

```pgsql
-- 创建一个角色 R1
CREATE ROLE R1;

-- 将查询 Student 表的权限授予角色 R1
GRANT SELECT ON TABLE Student TO ROLE R1;

-- 将角色 R1 授予用户 U1 和 U2
GRANT R1 TO U1, U2;
```

### 审计

审计是一种**事后检查**的安全机制。它把用户对数据库的所有操作自动记录下来，存入 **审计日志（Audit Trail）** ，便于事后分析和追查。通常通过 `AUDIT` 语句设置审计功能，通过 `NOAUDIT` 语句取消。

#### 审计

```pgsql
AUDIT <操作类型> [ , ... ]
[ ON <对象名> ]
[ BY { SESSION | ACCESS } ]
[ WHENEVER [ NOT ] SUCCESSFUL ];
```

| 成分                                    | 说明                                                               |
| --------------------------------------- | ------------------------------------------------------------------ |
| **`AUDIT`**                     | 开启审计                                                           |
| **`<操作类型>`**                | SQL语句类型，如 `TABLE`, `VIEW`, `SELECT`, `INSERT` 等     |
| **`[ON <对象名>]`**             | 指定审计的具体对象，如 `ON Student`；不指定则对所有对象有效      |
| **`[BY SESSION]`**              | 按**会话**审计：同一会话中，相同的操作只记录一次（默认方式） |
| **`[BY ACCESS]`**               | 按**访问**审计：每一次对该对象的访问都记录                   |
| **`[WHENEVER SUCCESSFUL]`**     | 只审计**执行成功**的操作                                     |
| **`[WHENEVER NOT SUCCESSFUL]`** | 只审计**执行失败**的操作                                     |

#### 取消审计

```pgsql
NOAUDIT <操作类型> [ ON <对象名> ];
```

## 关系代数

| 类别                       | 运算符                                       | 作用               |
| -------------------------- | -------------------------------------------- | ------------------ |
| **集合运算符**       | ∪（并）、-（差）、∩（交）、×（笛卡尔积）  | 从行的角度进行运算 |
| **专门的关系运算符** | σ（选择）、π（投影）、⋈（连接）、÷（除） | 同时涉及行和列     |
| **比较运算符**       | ＞、≥、＜、≤、＝、≠                       | 用于条件表达式     |
| **逻辑运算符**       | ¬（非）、∧（与）、∨（或）                 | 连接条件表达式     |

### 连接

$$
R ⋈_{AθB} S = σ_{AθB}(R × S)
$$

#### 等值连接

$$
\theta \text{为}=
$$

#### 自然连接

* 自然连接要求相等分量必须是同名的属性组，等值连接无此要求；
* 自然连接去掉重复属性列，等值连接不去掉

#### 外连接

* **悬浮元组** ：自然连接中被舍弃的元组。
* **外连接** ：将悬浮元组保留在结果中，其他属性填NULL。
* **左外连接** ：只保留左侧关系的悬浮元组。
* **右外连接** ：只保留右侧关系的悬浮元组。

#### 自身连接

关系与自身进行连接，需取别名区分

### 除

* 笛卡尔积的逆运算。
* R÷S结果包含 **只在R但不在S中的属性及其值** ，且这些元组与S的所有组合都在R中。

 **除法的步骤** ：

1. 确定R和S的公共属性列Y；
2. 计算R中所有非公共属性组X的值；
3. 对每个X值，求其在R中的 **象集** （即该X值对应所有Y值的集合）；
4. 找出所有象集**包含**了 S在Y上投影 的X值，即为R÷S的结果。

| 运算     | 记法         | 核心要点                              |
| -------- | ------------ | ------------------------------------- |
| 并       | R∪S         | 相同的属性个数和域，上下拼接          |
| 差       | R−S         | 相同属性，去掉共同行                  |
| 交       | R∩S         | = R−(R−S)，保留共同行               |
| 笛卡尔积 | R×S         | 每个元组排列组合，(n+m)列、k₁×k₂行 |
| 选择     | σ_F(R)      | 从行角度，WHERE条件                   |
| 投影     | π_A(R)      | 从列角度，去掉重复行                  |
| 连接     | R ⋈ S       | 从笛卡尔积+选择，θ连接               |
| 自然连接 | R ⋈ S       | 同名字段等值+去重列                   |
| 外连接   | ⟕ / ⟖ / ⟗ | 保留悬浮元组，填NULL                  |
| 除       | R÷S         | 象集包含S投影的元组                   |

## 范式

## ES图

## 其他

唯一决定关系的属性（集合）称为**候选码**。

候选码可选择的加一些无用的属性，成为**超码**，候选码是最小的超码。

候选码可以有很多，任意候选码的任意属性都是**主属性**，不能是任意候选码的主属性的属性是**非主属性**或**非码属性**。

许多候选码中选一个成为**主码**。

是整个表是唯一候选码时又称**全码**。

1NF：关系中的所有属性值都是 **不可再分的原子值** ，不允许嵌套表或集合。

学生(学号, 姓名, 选课列表)（选课列表是个数组）

2NF：满足 1NF，且 **不存在非主属性对候选码的部分函数依赖** 。

`选课成绩(学号, 课程号, 成绩, 学生姓名)`

* 候选键：(学号, 课程号)
* 非主属性：成绩、学生姓名
* 依赖关系：
  * (学号, 课程号) → 成绩（完全依赖，OK）
  * (学号, 课程号)→ 学生姓名（ **部分依赖** ，因为学号是候选键的真子集）

 **分解成2NF** ：

* 选课(学号, 课程号, 成绩)
* 学生(学号, 学生姓名)

3NF：满足 2NF，且 **不存在非主属性对候选码的传递函数依赖** 。

如果一个关系没有非主属性，那么它至少是3NF。

`学生(学号, 系名, 系主任)`

* 候选键：学号
* 依赖：学号 → 系名，系名 → 系主任
* 所以：学号 → 系主任 是传递依赖

BCNF：满足 3NF，且**不存在主属性对候选码的部分函数依赖和传递函数依赖**。

`STJ(S（学生）, T（教师）, J（课程）)`

`(S, J) -> T, (S, T) -> J, T -> J`

主属性是S，T，J，这里是J，候选码是 `(S, T)`，这里 `(S, T) -> J`是部分函数依赖。

数据库的基本特点：结构化，数据冗余度低，共享性高，独立性高，统一管理控制。

对于关系模式 R(U,F)**R**(**U**,**F**)，求候选码的一般步骤如下：

1. **分类属性** ：根据函数依赖集 F**F**，将属性分为四类：

* **L类** ：只出现在函数依赖左边（从未出现在右边）。
* **R类** ：只出现在函数依赖右边（从未出现在左边）。
* **LR类** ：既出现在左边又出现在右边。
* **N类** ：从未出现在任何函数依赖中。

1. **必选属性** ：L类和N类属性一定属于每一个候选码。
2. **构造闭包** ：从 L+N 出发，逐步添加 LR 类属性，计算闭包。若闭包等于全部属性 U**U**，则该组合是一个候选码。
3. **最小化** ：若某超码去掉任一属性后不再是超码，则为候选码。通常按属性数量递增尝试。
4. **重复** ：可能存在多个候选码，需检查不同的 LR 属性组合。

 **范式判定要点** （仅考虑非平凡函数依赖，且假定关系至少为1NF）：

* **2NF** ：消除非主属性对候选码的 **部分依赖** （即候选码的真子集不能决定非主属性）。
* **3NF** ：消除非主属性对候选码的 **传递依赖** （即非主属性不能依赖于其他非主属性）。
* **BCNF** ：每个函数依赖的左部都必须包含候选码（即左部必须是超键）。
