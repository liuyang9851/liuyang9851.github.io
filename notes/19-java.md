# Java笔记

## JDK（Java Developments Kit）Java开发工具包

- 开发工具

## JRE（Java Runtime Environment）

- 类库

## JVM（Java Virtual Machine）

- 解释器
- JIT（）编译器

## 编译与运行

- 编译：`javac MyClass.java`
- 运行：`java MyClass`

> 一个 `.java`文件中只能有一个公有类，不是只能有一个类。

## API文档

对应注释格式：`/**     内容     */`

## 变量命名

- 由字母、数字、下划线(`_`)、美元符号(`$`)组成

  1. 不能以数字开头
  2. 不能是Java关键字
  3. 区分大小写
- 变量/方法名：`camelCase`
- 常量名：`UPPER_SNAKE_CASE`
- 类名：`PascalCase`

## 基本数据类型

| 类型       | 大小  | 范围                | 默认值     | 示例                                             |
| ---------- | ----- | ------------------- | ---------- | ------------------------------------------------ |
| `byte`   | 1字节 | -128 ~ 127          | 0          | `byte b = 100;`                                |
| `short`  | 2字节 | -32,768 ~ 32,767    | 0          | `short s = 1000;`                              |
| `int`    | 4字节 | -2^31 ~ 2^31-1      | 0          | `int i = 100_000;`                             |
| `long`   | 8字节 | -2^63 ~ 2^63-1      | 0L (或 0l) | `long l = 100L;`                               |
| `float`  | 4字节 | 3.4E-38 ~ 3.4E+38   | 0.0f(F)    | `float f = 3.14f;`                             |
| `double` | 8字节 | 1.7E-308 ~ 1.7E+308 | 0.0d(D)    | `double d = 3.14;`<br />`double d = 3.14E2;` |

- `boolean`不能与任何数值类型互相转换

### 隐式类型转换

`byte → short → int → long → float → double`
`char → int`

## 输入

```java
Scanner input = new Scanner(System.in);
int a = input.nextInt();
double b = input.nextDouble();
String c = input.next();
```

## `instanceof()`

## 内存区域

### 栈内存 (Stack)

- **存储内容**：局部变量、方法调用帧、对象引用（地址）
- **特点**：
  - 线程私有，自动分配/释放
  - 基本类型存值，引用类型存堆地址
  - 速度较快，生命周期与方法/线程同步
- **示例**：`int[] arr` 中的 `arr` 引用

### 堆内存 (Heap)

- **存储内容**：所有 `new` 创建的对象（包括数组）
- **特点**：
  - 线程共享，由垃圾回收器 (GC) 管理
  - 数组本身是对象 → **数组对象实体存放在堆中**
- **示例**：`new int[10]` 创建的数组对象

### 常量池 (Constant Pool)

- **存储内容**：字符串字面量、`final` 常量、符号引用
- **特点**：
  - 属于方法区的一部分（Java 8 后位于元空间）
  - 相同字面量复用，节省内存
- **注意**：数组对象不存放在常量池

### 方法区 (Method Area)

- **存储内容**：类信息、静态变量、运行时常量池、即时编译代码
- **特点**：
  - JVM 规范中的**逻辑区域**，线程共享
  - Java 7 及以前由**永久代 (PermGen)** 实现（位于堆中）
  - Java 8 及以后由**元空间 (MetaSpace)** 实现（位于本地内存）
- **注意**：方法区是规范，元空间是实现

### 元空间 (MetaSpace) Java 8+ 新增

- **存储内容**：类的元数据（类名、方法、字段等）、运行时常量池、静态变量等（即方法区的内容）
- **特点**：
  - **独立于栈和堆**，使用本地内存（Native Memory）
  - 不再占用 Java 堆空间，避免 PermGen 的 `OutOfMemoryError`
  - 默认最大内存受本地内存限制，可通过 `-XX:MaxMetaspaceSize` 设置
  - 线程共享，由 GC 管理（可回收无用的类元数据）
- **与堆的关系**：物理上完全独立；逻辑上替代了永久代，作为方法区的实现

## `StringBuffer`

## 数组初始化

```java
Type[] a = {a_1, …, a_n};
Type[] a = new Type[n]{a_1, …, a_n};
Type[] a = new Type[n];
```

- 数组长度：`a.length`
- 数组越界会抛出 `ArrayIndexOutOfBoundsException`异常

### foreach型循环（可修改）

```java
for (int x : a) {
    System.out.print(x + " ");
}
```

- 值类型：拷贝
- 引用类型：引用（引用的拷贝）

### 多维数组

数组的数组（C#的交错数组，数组元素是数组，每行的元素个数可以不同）

```java
Type[][] a = new Type[m][];
Type[][] a = {{a_11, …, a_1n},{a_m1, …, a_mo}};
Type[][] a = new Type[m][]{{a_11, …, a_1n},{a_m1, …, a_mo}};
```

```java
for (int[] row : matrix) {        // row 的类型是 int[]
    for (int value : row) {       // value 的类型是 int
        System.out.print(value + " ");
    }
    System.out.println();
}
```

## 可变字符串

插入、追加、删除、替换等操作（堆中）

- 线程安全：`StringBuffer`（包含同步机制）
- 线程不安全：`StringBuilder`（无同步机制，但速度更快）

### 创建 `StringBuffer` 实例（`StringBuilder` 类似）

- `StringBuffer sb = new StringBuffer();` – 创建一个空的 `StringBuffer` 对象，不包含任何字符，长度为 0。
- `StringBuffer sb1 = new StringBuffer("Hello");`

### 使用 `StringBuffer`

- `sb.toString();` – 将 `StringBuffer` 的内容转换为 `String`
- `sb.append();` `sb.insert();` `sb.reverse();`
- `sb.setCharAt();` `sb.setLength();` – 设置 `StringBuffer` 长度
- 修改 `StringBuffer` 对象中指定位置的字符。
- `s1.concat(s2)` 把 `s2` 拼接到 `s1` 的后面

## 正则表达式 (Regular Expression，简写为regex)

| 函数                                                     | 作用                                                                                                          |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **`String` 类**                                  |                                                                                                               |
| `boolean matches(String regex)`                        | 测试字符串是否与给定的正则表达式匹配（完全相符）                                                              |
| `String replaceAll(String regex, String replaceStr)`   | 使用指定的替换字符串替换匹配正则表达式的所有子字符串                                                          |
| `String replaceFirst(String regex, String replaceStr)` | 使用指定的替换字符串替换匹配正则表达式的第一个子字符串                                                        |
| `String[] split(String regex)`                         | 用于将字符串根据指定的正则表达式进行分割，并返回分割后的子字符串数组                                          |
| **`Pattern` 类**                                 |                                                                                                               |
| `Pattern pattern = Pattern.compile(String regex)`      | 通过 `Pattern`类的静态方法 `compile()`创建一个 `Pattern`对象                                            |
| `Matcher matcher = pattern.matcher(String input)`      | 创建 `Matcher` 对象                                                                                         |
| **`Matcher` 类**                                 |                                                                                                               |
| `find()`                                               | 判断下一个匹配子串是否存在                                                                                    |
| `group()`                                              | 返回上一次与 `Pattern` 匹配的子串                                                                           |
| `start()`                                              | 返回上一次与 Pattern 匹配的子串在目标字符串中的起始位置                                                       |
| `end()`                                                | 返回上一次与 Pattern 匹配的子串在目标字符串中的结束位置<br />（即子序列在输入字符串中的结束位置的下一个索引） |
| `matches()`                                            | 判断整个目标字符串与正则表达式是否匹配                                                                        |
| `reset()`                                              | 用于将 Matcher 对象的匹配状态重置为其初始状态                                                                 |

```java
String str = "12345";
boolean isNumeric = str.matches("\\d+"); // 匹配一个或多个数字
System.out.println(isNumeric); // 输出 true

String str = "Hello World";
String replacedStr = str.replaceAll("\\s", "_"); // 将所有空格替换为下划线
System.out.println(replacedStr); // 输出 "Hello_World"

String str = "Hello World";
String replacedStr = str.replaceFirst("\\s", "_"); // 将第一个空格替换为下划线
System.out.println(replacedStr); // 输出 "Hello_World"

String str = "apple,banana,orange";
String regex = "[\\s\\p{Punct}]+"; // 定义了一个正则表达式，用于匹配一个或多个空白字符或标点符号。
String[] words = str.split(regex); // 使用 split() 方法将字符串 str 根据正则表达式 regex 进行分割，并将分割后的单词存储到数组 words 中
for (String word : words) {
    System.out.println(word);
}

String regex = "\\d+"; // 匹配一个或多个数字
String input = "12345";
Pattern pattern = Pattern.compile(regex); // 编译正则表达式
Matcher matcher = pattern.matcher(input); // 创建 Matcher 对象
boolean isMatch = matcher.matches(); // 调用方法，执行匹配操作

Matcher matcher = Pattern.compile("\\d+").matcher("Order123 costs 456 dollars");
while (matcher.find()) {
    System.out.println("Match: " + matcher.group() + ", Start: " + matcher.start() + ", End: " + matcher.end());
}
/* 输出：
Match: 123, Start: 5, End: 8
Match: 456, Start: 15, End: 18
*/
```

## 类修饰符

| 类修饰符     | 含义                                                                  |
| ------------ | --------------------------------------------------------------------- |
| `public`   | 可被任何对象访问                                                      |
| `abstract` | 抽象类，不能创建实例（但可以有构造方法或默认实现），与 `final` 冲突 |
| `final`    | 不能被继承的类，与 `abstract` 冲突                                  |
| 缺省         | 相同包中的对象才能访问                                                |

## 成员访问控制符

| 成员访问控制符 | 作用域                 |
| -------------- | ---------------------- |
| `public`     | 可被任何对象访问       |
| `protected`  | 同包中的类或自己的子类 |
| 缺省           | 同包中的类             |
| `private`    | 类内部                 |

## 各类别可用的访问修饰符

| 类别                                 | 包含的类型                                                                                      | 可用的访问修饰符                 | 说明                                        |
| ------------------------------------ | ----------------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------------- |
| **顶级类型**                   | 顶级类<br />顶级接口<br />顶级枚举<br />顶级记录（record）                                      | `public` 或 包私有（无修饰符） |                                             |
| **静态嵌套类型**               | `static` 内部类<br /> `static` 内部接口<br /> `static` 内部枚举<br /> `static` 内部记录 | 四种全部可用                     | 行为类似顶级类型，但可写在外部类中          |
| **成员内部类<br />（非静态）** | 普通内部类（无 `static`）                                                                     | 四种全部可用                     | 隐式持有外部类 `this`，可访问外部所有成员 |
| **局部类型**                   | 局部内部类（方法内定义）<br />局部枚举（Java 16+）<br />局部记录（Java 16+）                    | 无修饰符                         | 作用域仅在方法内，不能被修饰符控制          |
| **匿名类**                     | 匿名内部类（表达式）                                                                            | 无修饰符                         | 一次性使用，无权声明任何修饰符              |

- **顶级 / 静态嵌套**：不依赖外部实例 → 可见性范围由包 + 访问修饰符控制，规则一致。
- **成员内部类**：依赖外部实例 → 访问修饰符作用与普通成员相同，但类本身也可被 `private` 等修饰。
- **局部 / 匿名**：瞬间存在，不可复用 → 无访问修饰符概念。

## 类型修饰符互斥与规则

| 类型                                         | `final`            | `abstract`       | `static`（修饰自身）        | 关键规则 / 互斥                                                                   |
| -------------------------------------------- | -------------------- | ------------------ | ----------------------------- | --------------------------------------------------------------------------------- |
| **顶级类**                             | ✔                   | ✔                 | ✘（无意义）                  | `final` 与 `abstract` 互斥                                                    |
| **静态嵌套类**                         | ✔                   | ✔                 | ✔（已是 `static`，可省略） | 同上，且 `static` 必须显式（否则成为成员内部类）                                |
| **成员内部类<br />（非静态）**         | ✔                   | ✔                 | ✘（不能写 `static`）       | 不能有静态成员（除编译时常量）<br />但可以定义static final 的基本类型或字符串常量 |
| **局部内部类 <br />（定义在方法内）** | ✔                   | ✔                 | ✘（不能写 `static`）       | 不能有静态成员；可访问 `final` / `effectively final` 局部变量                 |
| **匿名类**                             | ✘（隐式 final）     | ✘（不能是抽象类） | ✘                            | 不能显式 `final`（但不可被继承）；不能声明构造方法                              |
| **顶级接口**                           | ✘                   | ✔（隐式）         | ✘（修饰自身无意义）          | 接口隐式 `abstract`；不能 `final`                                             |
| **静态嵌套接口**                       | ✘                   | ✔（隐式）         | ✔（必须显式 `static`）     | 同顶级接口，但可放在类中                                                          |
| **成员内部接口<br />（非静态）**       | ✘                   | ✔（隐式）         | ✘（禁止）                    | 成员接口隐式 `static`（Java 规范），实际无需也不能写                            |
| **枚举**                               | ✔（不允许子类）     | ✘                 | ✔（静态成员）                | 枚举隐式 `final`（但不能自己写 `final`）；构造器 `private`                  |
| **记录（record）**                     | ✔（隐式 `final`） | ✘                 | ✔（静态成员）                | 记录隐式 `final`；不能声明实例字段以外的额外字段                                |

- `static` 的意义：仅用于“嵌套类型是否独立于外部实例”。**顶级类型永远不会写 `static`**。
- `final` 与 `abstract` 互斥适用于所有类和枚举（接口、记录已限定）。
- 成员内部接口隐式 `static`，因为非静态内部接口无意义（接口不能持有外部类引用）。

## 其他成员变量修饰符

| 其他成员变量修饰符 | 作用                                                                                                                                                                                                                                                       |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `static`         |                                                                                                                                                                                                                                                            |
| `final`          | 必须在**声明时**、**实例初始化块**或**每个构造方法中**完成赋值，之后不能更改<br />与 `static` 配合时，代表必须在**声明时**或**静态初始化块**中赋值<br />（在局部变量中，可以在先声明后**在某处（使用前）赋值一次**） |

## 其他成员方法修饰符

| 其他成员方法修饰符 | 作用                                                                                           |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| `static`         | 不能被子类重写（override）                                                                     |
| `final`          | 无法被子类重写（override）和隐藏<br />仍可以被重载（Overload）和继承<br />与 `abstract` 冲突 |
| `abstract`       | 与 `final` 冲突                                                                              |

## 重载、重写与隐藏

| 概念                  | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 重载（Overload）      | 被称为编译时多态，因为具体调用哪个函数在编译期确定<br />理论上是只能限于一个类中（但子类中可以“重载”，且不受父类 `final` 的限制）                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 重写/覆盖（Override） | 支持多态（父类引用.方法调用的是子类方法）<br />构造方法不能被重写，不能被隐藏<br />可用 `@Override` 注解<br />返回类型可以是原返回类型的子类（协变）<br />访问权限不能比父类更严格（可以更宽松）<br />父类方法不能是 `final` 或 `private` 或 `static`<br />实例方法不能被静态方法重写<br />~~子类声明的异常：与父类相同或是父类异常的子类~~<br />声明检查异常：与父类相同或是父类异常的子类<br />private方法不存在重写的概念<br />没被static或private修饰的方法会执行动态绑定，在运行时根据虚表调用对象实际所属类的方法<br />否则在编译期确定调用引用对应类的方法。 |
| 隐藏（Hide）          | 不支持多态（父类引用.方法调用的是父类方法）<br />实例方法不能被隐藏<br />静态方法才能被隐藏<br />新方法必须也是静态方法<br />访问权限不能比父类更严格（可以更宽松）<br />private方法不存在隐藏的概念                                                                                                                                                                                                                                                                                                                                                                         |

|            | 重载（Overload） | 重写/覆盖（Override） | 隐藏（Hide）         |
| ---------- | ---------------- | --------------------- | -------------------- |
| 方法名     | 相同             | 相同                  | 相同                 |
| 参数列表   | 不同             | 相同                  | 相同                 |
| 返回值     | 任意             | 协变                  | 任意                 |
| 访问修饰符 | 任意             | 子类不能比父类更严格  | 子类不能比父类更严格 |

父类方法 `private`：全新方法

参数列表不同：重载
参数列表相同：参考下表

| 父类方法类型 | 子类方法类型 | 结果                      | 示例                                                  |
| ------------ | ------------ | ------------------------- | ----------------------------------------------------- |
| 实例方法     | 实例方法     | **重写 (Override)** | `void m()` → `void m()`                          |
| 静态方法     | 静态方法     | **隐藏 (Hide)**     | `static void m()` → `static void m()`            |
| 实例方法     | 静态方法     | **编译错误**        | `void m()` → `static void m()`（不可重写为静态） |
| 静态方法     | 实例方法     | **编译错误**        | `static void m()` → `void m()`（不可隐藏为实例） |

## `this` 与实例

- `this`：类的对应实例（不能在 `static` 中使用）
- 实例（Instance），属性（Field），方法（Method）
- Java中没有静态类，但静态属性或方法可以通过 `类名.静态属性` 或 `类名.静态方法()` 访问。

## 构造方法/构造器

- 无返回值。
- 类没有显式编写构造方法时会创建默认的无参构造方法。
- 若类只显式编写了有参构造方法则不会创建无参构造方法。
- 子类的构造方法的最终运行若没有主动调用父类构造方法，则必然尝试调用父类的无参构造方法，如果父类不存在无参构造方法，则会在编译期报错。
- 子类通过 `super()` 调用父类构造函数时，必须放在子类构造函数的第一行，否则有编译期错误。
- 不能被重写和隐藏，能被重载。

## 初始化代码块

### 实例初始代码块

- 由 `{…}` 括起来的代码块，做为类成员放在类中
- 在初始化对象（调用构造函数）前，执行初始化列表中的代码块。在父类构造调用之后，本类构造方法体之前
- 每次调用构造方法前都会执行

### 静态初始化代码块

- 由 `static{…}` 括起来的代码块，作为类成员放在类中
- 在 ClassLoader 加载类之前由 JVM 自动调用该代码块中的代码
- 只执行一次，与创建的对象个数无关

```java
public class InitTest {
    static { // 静态初始化代码块
        System.out.print("A ");
    }
    { // 实例初始代码块
        System.out.print("B ");
    }
    public InitTest() { // 构造方法
        System.out.print("C ");
    }
    public static void main(String[] args) {
        System.out.print("D ");
        InitTest t1 = new InitTest();
        InitTest t2 = new InitTest();
    } // A D B C B C
}
```

## `==` 与 `.equals()`

- `==` 永远比较值/引用（比较 `String` 时也会相等）
- `new` 出来的 `String` 用 `==` 比较不相同，`.equals()` 会相同。
- `.equals()` 对 `String` 和包装类会比较实际内容，可重写。
- 重写 `equals()` 方法的有包装类，字符串类，时间类，文件/路径类，容器/集合类。

## 包装类与缓存

Java 对 `Integer` 的自动装箱使用缓存机制：**-128 到 127** 范围内的值会从缓存中返回同一对象。

使用 `new Integer(10)` 会强制在堆内存中创建一个新对象，不使用缓存池。而 `Integer b = 10` 会使用缓存池中的对象。

```java
Integer count = null;
if (count > 0) { // 运行时抛出 NullPointerException
    System.out.println("Positive");
}

Integer i = 10; Long l = 20L; Double d = 5.5;
Object result = i + l + d; // result是Object类型的引用，指向一个Double对象
System.out.println(result.getClass().getName()); // getClass()是对应被引用的类型而非引用的类型
```

| 基本类型    | 包装类      | 装箱方法                     | 拆箱方法                   |
| ----------- | ----------- | ---------------------------- | -------------------------- |
| `int`     | `Integer` | `Integer.valueOf(int)`     | `Integer.intValue()`     |
| `double`  | `Double`  | `Double.valueOf(double)`   | `Double.doubleValue()`   |
| `boolean` | `Boolean` | `Boolean.valueOf(boolean)` | `Boolean.booleanValue()` |

## 垃圾回收

`System.gc()` 或 `Runtime.getRuntime().gc()` 建议JVM进行垃圾回收。

当垃圾回收器将要释放无用对象的内存时，会先调用该对象的 `finalize()` 方法再回收，在Java 9中被废弃。

## `Object` 类

所有类都直接或间接继承了 `java.lang.Object`，除非它显式继承另一个类。

### Java的多态性体现

- 编译时多态性：方法重载 (Method Overloading)
- 运行时多态性：方法重写 (Method Overriding)：子类重写其父类中的方法；父类引用指向子类对象；接口引用，不同的实现。

### `instanceof` 运算符

`instanceof` 是二元运算符。在运行时测试左边的对象是否是右边类（或接口）的实例。编译时要求左边的变量类型与右边的类型存在**继承或实现关系**，否则编译错误。对 `null` 使用 `instanceof` 总是返回 `false`。`null` 只能放在左边。

### Object类的常用方法

| 方法                                    | 作用                                                                                                      |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `toString()`                          | 返回对象的字符串表示。<br />默认是“类名@哈希码十六进制”，通常建议重写。                                 |
| `equals(Object obj)`                  | 判断两个对象是否“相等”。<br />默认与 `==` 相同（比较引用），通常需要重写。                            |
| `hashCode()`                          | 返回对象的哈希码值，用于基于哈希的集合（如 `HashMap`）。<br />重写 `equals` 时必须重写 `hashCode`。 |
| `getClass()`                          | 返回对象的运行时类（`Class` 对象），常用于反射。                                                        |
| `clone()`                             | 创建并返回对象的副本。需要实现 `Cloneable` 接口，<br />否则抛出 `CloneNotSupportedException`。        |
| `finalize()`                          | 垃圾回收前调用，用于资源清理。从 Java 9 开始已弃用，不推荐使用。                                          |
| `wait()` <br />`wait(long timeout)` | 让当前线程等待，直到被 `notify()` 或 `notifyAll()` 唤醒。用于线程同步。                               |
| `notify()` <br />`notifyAll()`      | 唤醒一个或所有等待该对象监视器的线程。                                                                    |

### `Class` 类的常用方法

| 方法                                                   | 作用                                                                                    |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| `getName()`                                          | 返回类的全限定名（包名+类名）<br />对于默认包/无名包，只返回类名                        |
| `getSimpleName()`                                    | 返回类名（不含包）                                                                      |
| `getSuperclass()`                                    | 返回父类的 `Class` 对象<br />Object类调用这个返回null                                 |
| `getInterfaces()`                                    | 返回实现的接口的 `Class` 数组                                                         |
| `getModifiers()`                                     | 返回修饰符（如 `public`、`abstract`）的整数位掩码                                   |
| `newInstance()`                                      | 调用无参构造创建实例<br />（已过时，推荐用 `getDeclaredConstructor().newInstance()`） |
| `getDeclaredFields()`                                | 获取所有声明的字段（包含私有）                                                          |
| `getDeclaredMethods()`                               | 获取所有声明的方法                                                                      |
| `getDeclaredConstructors()`                          | 获取所有声明的构造方法                                                                  |
| `getField(String name)`                              | 获取指定名称的公共字段                                                                  |
| `getMethod(String name, Class<?>... parameterTypes)` | 获取指定名称和参数的公共方法                                                            |
| `isArray()`                                          | 判断是否为数组类                                                                        |
| `isPrimitive()`                                      | 判断是否为基本类型（`int.class` 等）                                                  |
| `isEnum()`                                           | 判断是否为枚举类                                                                        |
| `cast(Object obj)`                                   | 将对象强制转换为该 `Class` 所代表的类型                                               |

## 抽象类

抽象类可以包含字段，构造方法，抽象实例方法，具体实例方法，具体静态方法。抽象方法不能被 `private`，`static` 和 `final` 修饰，因为这三种修饰代表子类不能重写。

## 接口

```java
[修饰符] interface 接口名 extends 父接口列表
```

一个类继承了两个接口，其中一个接口有默认方法，另一个接口中包含相同声明的默认方法，这会导致冲突，Java 不知道该使用哪一个。为了解决这个问题，实现类必须重写该方法，使用：`父接口名.super.默认方法名()`

### 接口成员一览

| 成员类型 | 关键字 / 示例                                     | 隐含修饰符              | 使用说明                               |
| -------- | ------------------------------------------------- | ----------------------- | -------------------------------------- |
| 抽象方法 | `void method();`（abstract 可以省略）           | `public abstract`     | 没有方法体，必须由实现类实现，可被重写 |
| 默认方法 | `default void method() {}`                      | `public`              | 包含方法体，提供默认实现，可被重写     |
| 静态方法 | `static void method() {}`                       | `public`              | 包含方法体，可通过接口名调用           |
| 私有方法 | `private void helper() {}`                      | 必须显式                | 包含方法体，仅限接口内部调用           |
| 常量字段 | `int CONST = 42;`（public static final 可省略） | `public static final` | 必须初始化，不能修改                   |
| 内部类   | `class Inner {}`                                | `public static`       |                                        |
| 内部接口 | `interface Inner {}`                            | `public static`       |                                        |
| 枚举类   | `enum Status { A, B }`                          | `public static`       |                                        |

### 类成员（普通类）一览

| 成员类型                   | 关键字 / 示例                  | 隐含修饰符                    | 使用说明                                                            |
| -------------------------- | ------------------------------ | ----------------------------- | ------------------------------------------------------------------- |
| 实例字段                   | `int x;`                     | 包私有                        | 每个对象独立存储，可通过对象访问                                    |
| 静态字段                   | `static int count;`          | 包私有                        | 属于类，所有实例共享，通过类名访问                                  |
| 常量字段                   | `static final int MAX = 10;` | 需显式声明（通常 `public`） | 值不可变，编译时常量                                                |
| 实例方法                   | `void method() {}`           | 包私有                        | 可访问实例成员和静态成员                                            |
| 静态方法                   | `static void method() {}`    | 包私有                        | 只能访问静态成员，不能访问实例成员                                  |
| 抽象方法                   | `abstract void method();`    | 包私有                        | 无方法体，必须在具体子类中实现（仅抽象类可含）                      |
| 构造方法                   | `ClassName() {}`             | 包私有                        | 与类同名，无返回值，用于初始化对象                                  |
| 实例初始化块               | `{ ... }`                    | 无                            | 每次调用构造方法前执行                                              |
| 静态初始化块               | `static { ... }`             | 无                            | 类加载时执行一次，用于初始化静态字段                                |
| 成员内部类<br />（非静态） | `class Inner {}`             | 包私有                        | 持有外部类 `this` 引用，可访问外部类所有成员                      |
| 静态嵌套类                 | `static class Nested {}`     | 包私有                        | 不持有外部类引用，行为类似顶级类                                    |
| 局部内部类                 | 方法内定义 `class Local {}`  | 无修饰符                      | 作用域仅在方法内，可访问 `final` / `effectively final` 局部变量 |
| 匿名内部类                 | `new Interface() { ... }`    | 无修饰符                      | 一次性使用，不能定义构造方法                                        |

## 枚举

枚举类是一种特殊的类，它默认继承了 `java.lang.Enum` 类，其中 `Enum` 类实现了 `java.lang.Serializable` 和 `java.lang.Comparable` 两个接口。无法在运行时添加或删除实例。

枚举类中的所有常量在类加载时就会被实例化，而不是等到使用时才创建。每有一个枚举常量就会调用一次构造方法。

枚举类如果准备实现接口，就必须选择由枚举类提供统一实现或由枚举类的所有枚举常量都提供自己的实现。

```java
interface Action {
    void run();
}
enum Status implements Action {
    START { public void run() { System.out.print("1"); } },
    STOP  { public void run() { System.out.print("2"); } };
    private Status() { System.out.print("0"); }
}
public class Test {
    public static void main(String[] args) {
        Status.START.run();
        Status.STOP.run();
    }
} // 0012
```

### 枚举成员一览

| 成员类型     | 关键字 / 示例                                  | 隐含修饰符                 | 使用说明                                                 |
| ------------ | ---------------------------------------------- | -------------------------- | -------------------------------------------------------- |
| 枚举常量     | `RED, GREEN, BLUE;`                          | `public static final`    | 枚举类的预定义实例，类型为枚举自身                       |
| 实例字段     | `private int value;`                         | 无（通常显式 `private`） | 每个常量可拥有不同的字段值，通常声明为 `private final` |
| 构造方法     | `Color(int v) { value = v; }`                | `private`（可省略）      | 必须为 `private`，不能手动调用，用于初始化枚举常量     |
| 实例方法     | `public int getValue() { return value; }`    | 包私有                     | 可被枚举常量调用，通常声明为 `public`                  |
| 静态方法     | `public static Color fromInt(int v) { ... }` | 包私有                     | 可通过枚举名调用，如 `Color.values()` 是编译器自动生成 |
| 常量特定方法 | `RED { public void action() {...} }`         | 无                         | 为单个常量单独重写方法（通过匿名内部类实现）             |
| 静态初始化块 | `static { ... }`                             | 无                         | 类加载时执行一次，用于初始化静态字段                     |

## 异常（Exception）

异常（Exception）是指在执行期间中断程序指令正常流程的事件。当方法中出现异常情况时，该方法会创建一个异常对象并将其传递给运行时系统。异常对象包含有关错误的信息，包括错误的类型和错误发生时程序的状态。

- **错误（Error）**：是指程序在执行过程中所遇到的硬件或操作系统的错误，是致命的，需外界干预。如：堆栈溢出错误、内存不足错误、虚拟机错误等。
- **异常（Exception）**：程序遇到的运行时错误。如：数组越界、除数为0、操作数超出数据范围等。

语法错误不属于Error或Exception。运行时错误既有Error又有Exception。逻辑错误是能跑通但不符合预期。

```
java.lang.Throwable
    ├── java.lang.Error
    │       ├── OutOfMemoryError
    │       ├── StackOverflowError
    │       └── ...
    └── java.lang.Exception
            ├── IOException
            ├── SQLException
            ├── RuntimeException
            │       ├── NullPointerException
            │       ├── IllegalArgumentException
            │       ├── IndexOutOfBoundsException
            │       └── ...
            └── ...
```

### 异常的传播

异常从发生异常的方法逐渐向外传播，首先传给该方法的调用者，该方法调用者再次传给其调用者……直至最后传到 main 方法，如果 main 方法依然没有处理该异常，JVM 会中止该程序，并打印异常的跟踪栈信息。信息是先打印内部后打印外部。

```java
public class ExceptionStackDemo {
    // 最底层方法：抛出异常
    public static void methodC() {
        System.out.println("methodC 开始执行");
        // 这里制造一个异常
        throw new RuntimeException("methodC 中出现异常");
    }
    // 中间层方法：调用 methodC，但不处理异常
    public static void methodB() {
        System.out.println("methodB 开始执行");
        methodC();                  // 异常在这里抛出，但 methodB 没有 try-catch
        System.out.println("methodB 结束（这句不会执行）");
    }
    // 最外层方法：调用 methodB，并准备捕获异常
    public static void methodA() {
        System.out.println("methodA 开始执行");
        try {
            methodB();
        } catch (RuntimeException e) {
            System.out.println("methodA 捕获到异常: " + e.getMessage());
        }
        System.out.println("methodA 处理完异常，继续执行");
    }
    public static void main(String[] args) {
        methodA();
    }
}
/*
methodA 开始执行
methodB 开始执行
methodC 开始执行
methodA 捕获到异常: methodC 中出现异常
methodA 处理完异常，继续执行
*/
```

### 主动抛出异常/错误

`throw new Exception/Error("说明");`

### 异常类中包含的方法

- `getMessage()`：返回该异常的详细描述字符串。
- `printStackTrace()`：将该异常的跟踪栈信息输出到标准错误输出。
- `printStackTrace(PrintStream s)`：将该异常的跟踪栈信息输出到指定输出流。
- `getStackTrace()`：返回该异常的跟踪栈信息。

### 受检异常（Checked Exception）

受检异常（Checked Exception）是指必须被显式处理（`try-catch`）或声明（`throws`）（即拖延问题，传给上级）的异常。它们继承自 `Exception` 但不是 `RuntimeException` 的子类。

捕获受检异常时catch 声明的异常类型应比方法实际抛出的异常类型更宽松（即父类或相同类型）。

```java
import java.io.*;

public class CheckedExceptionDemo {
    public static void main(String[] args) {
        // 方式1：try-catch 处理
        try {
            FileReader fr = new FileReader("test.txt");
        } catch (FileNotFoundException e) {
            System.out.println("文件未找到: " + e.getMessage());
        }

        // 方式2：声明抛出（在方法上）
        try {
            readFile();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // 声明抛出受检异常
    public static void readFile() throws IOException {
        FileReader fr = new FileReader("test.txt");
    }
}
```

| 异常类                         | 说明                                            | 常见场景                                         |
| ------------------------------ | ----------------------------------------------- | ------------------------------------------------ |
| `IOException`                | I/O 操作失败或中断                              | 文件读写、网络通信                               |
| `FileNotFoundException`      | 文件不存在或无法打开                            | `FileInputStream`、`FileReader`              |
| `EOFException`               | 输入过程中意外到达文件末尾                      | `DataInputStream` 读取                         |
| `SQLException`               | 数据库访问错误                                  | JDBC 操作                                        |
| `ClassNotFoundException`     | 类加载器找不到指定的类                          | `Class.forName()`、`ClassLoader.loadClass()` |
| `InterruptedException`       | 线程被中断                                      | `Thread.sleep()`、`wait()`                   |
| `ParseException`             | 字符串解析错误                                  | `SimpleDateFormat`、`MessageFormat`          |
| `MalformedURLException`      | URL 格式不合法                                  | 创建 `URL` 对象                                |
| `NoSuchMethodException`      | 反射调用时找不到方法                            | `Class.getMethod()`                            |
| `NoSuchFieldException`       | 反射时找不到字段                                | `Class.getField()`                             |
| `InstantiationException`     | 反射创建实例失败（抽象类、接口等）              | `Class.newInstance()`                          |
| `IllegalAccessException`     | 反射访问权限不足                                | 私有构造器或字段                                 |
| `CloneNotSupportedException` | 对象未实现 `Cloneable` 接口却调用 `clone()` | `Object.clone()`                               |

### `finally` 示例

`finally` 块的执行时机是在 `try` 或 `catch` 块执行完“离开生命周期”之前。

如果在finally快中执行return，会导致立即跳出try-catch-finally语句，try和catch中的返回值被finally中的覆盖。

try-catch-finally可以在任意部分里面嵌套。内层 `finally` 的 `return` 不会不会直接跳出外层，外层 `finally` 仍然会照常运行。

```java
public class FinallyTest {
    public static String checkResource() {
        try {
            System.out.print("Open-");
            throw new Exception();
            System.out.print("AfterException-");
            return "Result-";
        } catch (Exception e) {
            return "Error-";
        } finally {
            System.out.print("Close-");
        }
    }

    public static void main(String[] args) {
        System.out.print(checkResource()); // Open-Close-Error-
    }
}
```

### 多异常捕获

```java
catch(异常1 | 异常2 | 异常3 ex) {
    // 多个异常之间用竖线隔开。
    // 异常变量之前有隐式 final 修饰
}
```

### `try-with-resources`

使用 `try-with-resources` 语句自动关闭资源，可以关闭：流、连接或任何实现 `java.io.Closeable` 或其父类 `java.io.AutoCloseable` 接口的类。在 `try-with-resources` 语句中，资源的 `close()` 方法会在 `try` 块执行完毕或发生异常时立即调用，且早于 `catch` 和 `finally` 块执行。

```java
try (FileReader fr = new FileReader("test.txt")) {
    System.out.println((char)fr.read());
    int i = 1 / 0; // 模拟读取时出错
} catch (Exception e) {
    System.out.println("捕获错误: " + e.getMessage());
}
```

```java
class MyResource implements AutoCloseable {
    public void close() { System.out.print("Closed "); }
}
public class TryWithResourcesTest {
    public static void main(String[] args) {
        try (MyResource res = new MyResource()) {
            System.out.print("Using ");
            int x = 10 / 0; // 产生异常
        } catch (Exception e) {
            System.out.print("Error ");
        } finally {
            System.out.print("Finally ");
        }
    } // Using Closed Error Finally
}
```

## 流（Stream）

### 分类

#### 按照流的方向

- 输入流：数据只能从外部源流入程序，而不能向其写出数据（InputStream/Reader）（具体来说数据是从外界流入调用者）
- 输出流：数据只能从程序流出到外部目标，而不能从中读取数据（OutputStream/Writer）（具体来说数据是从调用者流出外界）

#### 按照流的数据单元

- 字节流：基本数据单元是字节（InputStream/OutputStream）
- 字符流：基本数据单元是字符（Reader/Writer）

#### 按照流的角色

- 节点流：直接与IO设备进行交互（File/Arrat/Piped/String）
- 处理流：对已有的流进行拼接或封装，再与 IO 设备交互

### 输入字节流（InputStream）

```
java.lang.Object
  └─ java.io.InputStream (抽象类)
       ├─ ByteArrayInputStream
       ├─ FileInputStream
       ├─ FilterInputStream
       │    ├─ BufferedInputStream
       │    ├─ DataInputStream
       │    └─ PushbackInputStream
       ├─ ObjectInputStream
       ├─ PipedInputStream
       ├─ SequenceInputStream
       └─ (其他) AudioInputStream, CipherInputStream, ZipInputStream 等（扩展包）
```

### 输出字节流（OutputStream）

```
java.lang.Object
  └─ java.io.OutputStream (抽象类)
       ├─ ByteArrayOutputStream
       ├─ FileOutputStream
       ├─ FilterOutputStream
       │    ├─ BufferedOutputStream
       │    ├─ DataOutputStream
       │    └─ PrintStream
       ├─ ObjectOutputStream
       ├─ PipedOutputStream
       └─ (其他) CipherOutputStream, ZipOutputStream 等
```

### 输入字符流（Reader）

```
java.lang.Object
  └─ java.io.Reader (抽象类)
       ├─ BufferedReader
       │    └─ LineNumberReader (已过时，建议用 BufferedReader)
       ├─ CharArrayReader
       ├─ FilterReader
       │    └─ PushbackReader
       ├─ InputStreamReader (字节→字符桥接)
       │    └─ FileReader
       ├─ PipedReader
       ├─ StringReader
       └─ (其他) CipherReader, ZipReader 等（较少用）
```

### 输出字符流（Writer）

```
java.lang.Object
  └─ java.io.Writer (抽象类)
       ├─ BufferedWriter
       ├─ CharArrayWriter
       ├─ FilterWriter (抽象类，无直接子类)
       ├─ OutputStreamWriter (字符→字节桥接)
       │    └─ FileWriter
       ├─ PipedWriter
       ├─ PrintWriter
       ├─ StringWriter
       └─ (其他) CipherWriter 等
```

### 流分类汇总表

| 分类                                               | 字节输入流<br />InputStream                                     | 字节输出流<br />OutputStream                                       | 字符输入流<br />Reader | 字符输出流<br />Writer | 节点/处理流 |
| -------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------- | ---------------------- | ----------- |
| 抽象基类                                           | InputStream                                                     | OutputStream                                                       | Reader                 | Writer                 | 抽象基类    |
| 文件<br />File                                     | FileInputStream                                                 | FileOutputStream                                                   | FileReader             | FileWriter             | 节点流      |
| 数组<br />Array                                    | ByteArrayInputStream                                            | ByteArrayOutputStream                                              | CharArrayReader        | CharArrayWriter        | 节点流      |
| 管道<br />Piped                                    | PipedInputStream                                                | PipedOutputStream                                                  | PipedReader            | PipedWriter            | 节点流      |
| 字符串<br />String                                 |                                                                 |                                                                    | StringReader           | StringWriter           | 节点流      |
| 缓冲流<br />Buffered<br />提供缓冲区<br />提高性能 | BufferedInputStream                                             | BufferedOutputStream                                               | BufferedReader         | BufferedWriter         | 处理流      |
| 转换流                                             |                                                                 |                                                                    | InputStreamReader      | OutputStreamWriter     | 处理流      |
| 过滤流<br />Filter                                 | FilterInputStream<br />DataInputStream<br />BufferedInputStream | FilterOutputStream<br />DataOutputStream<br />BufferedOutputStream | FilterReader           | FilterWriter           | 处理流      |
| 打印流<br />Print                                  |                                                                 | PrintStream                                                        |                        | PrintWriter            | 处理流      |
| 推回流<br />Pushback                               | PushbackInputStream                                             |                                                                    | PushbackReader         |                        | 处理流      |
| 对象流<br />Object                                 | ObjectInputStream                                               | ObjectOutputStream                                                 |                        |                        | 处理流      |

### InputStream 常用方法

| 方法                                        | 功能说明                                                                                                                            |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `int read()`                              | 读取一个byte并返回；若没有数据，返回-1                                                                                              |
| `int read(byte[] b)`                      | 读取多个byte到byte数组中，并返回读取的字节数                                                                                        |
| `int read(byte[] b, int offset, int len)` | 读取len个bytes到byte数组中，数据从数组的offset开始，并返回读取的字节数                                                              |
| `int available()`                         | 返回输入流中可读取的字节数                                                                                                          |
| `long skip(long n)`                       | 移动位置指针，使它从当前位置后跳过n个字节                                                                                           |
| `void mark(int readlimit)`                | 在当前位置做标记，并在读取readlimit字节数后标记作废，用reset可以回到这个标记，<br />但读取超过readlimit这个字节数，这个标记不起作用 |
| `void reset()`                            | 重置输入流，位置指针回到标记位置                                                                                                    |
| `void close()`                            | 关闭输入流                                                                                                                          |

### OutputStream 常用方法

| 方法                                          | 功能说明                                                   |
| --------------------------------------------- | ---------------------------------------------------------- |
| `void write(int b)`                         | 将b的低位字节写入输出流（将int转换为字节）                 |
| `void write(byte[] b)`                      | 将字节数组b的全部字节按顺序写到输出流中                    |
| `void write(byte[] b, int offset, int len)` | 将字节数组b中从offset位置开始的len个数据顺序地写入到输出流 |
| `void flush()`                              | 强制清空输出缓冲区并执行向外设写操作                       |
| `void close()`                              | 关闭输出流                                                 |

### FileInputStream 构造方法

| 构造方法                               | 说明                                               |
| -------------------------------------- | -------------------------------------------------- |
| `FileInputStream(String name)`       | 通过文件路径名创建输入流，打开一个实际文件的连接。 |
| `FileInputStream(File file)`         | 通过File对象创建输入流，打开一个实际文件的连接。   |
| `FileInputStream(FileDescriptor fd)` | 通过文件描述符创建输入流，对应已打开文件的连接。   |

### FileOutputStream 构造方法

| 构造方法                                          | 说明                                                                                        |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `FileOutputStream(String name)`                 | 通过文件路径名创建输出流，文件将被覆盖（从头开始写）。                                      |
| `FileOutputStream(String name, boolean append)` | 通过文件路径名创建输出流。若append为true，数据追加到文件末尾；<br />若为false，覆盖原文件。 |
| `FileOutputStream(File file)`                   | 通过File对象创建输出流，文件将被覆盖。                                                      |
| `FileOutputStream(FileDescriptor fd)`           | 通过文件描述符创建输出流，对应已打开文件的连接。                                            |

### DataInputStream 方法

| 方法                                | 说明                                                   |
| ----------------------------------- | ------------------------------------------------------ |
| `DataInputStream(InputStream in)` | 创建一个数据输出流，将数据写入指定的 `OutputStream`  |
| `Xxx readXxx()`                   | 从流中读取一个Xxx类型的数据（Boolean/Int/Char/Double） |
| 从 `InputStream` 中继承下来的方法 |                                                        |

### DataOutputStream 方法

| 方法                                   | 说明                                                     |
| -------------------------------------- | -------------------------------------------------------- |
| `DataOutputStream(OutputStream out)` | 创建一个数据输入流，从指定的 `InputStream` 读取数据    |
| `Xxx writeXxx()`                     | 将一个Xxx类型的数据写入输出流（Boolean/Int/Char/Double） |
| 从 `OutputStream` 中继承下来的方法   |                                                          |

### System 类中的字段

| 字段           | 类型                                                | 说明           |
| -------------- | --------------------------------------------------- | -------------- |
| `System.in`  | `InputStream`（被包装为 `BufferedInputStream`） | 标准输入流     |
| `System.out` | `PrintStream`                                     | 标准输出流     |
| `System.err` | `PrintStream`                                     | 标准错误输出流 |

### Reader 常用方法

| 方法                                        | 说明                                                                                                           |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `int read()`                              | 读取单个字符。返回该字符的 Unicode 编码（0-65535）；<br />如果到达流末尾，返回 -1。                            |
| `int read(char[] cbuf)`                   | 将字符串读入数组。返回实际读取的字符个数；如果到达流末尾，返回 -1。                                            |
| `int read(char[] cbuf, int off, int len)` | 将字符串读入数组的某一部分。从 off 位置开始存放，最多读取 len 个字符。                                         |
| `long skip(long n)`                       | 跳过 n 个字符。返回实际跳过的字符数。                                                                          |
| `boolean ready()`                         | 判断流是否准备好被读取。如果缓冲区不为空，<br />或者底层流有可用数据，则返回 true。                            |
| `void mark(int readLimit)`                | 标记流中的当前位置。后续可以通过 reset() 回到此处。<br />readLimit 指定在标记处之前允许读取的最大字符数。      |
| `boolean markSupported()`                 | 判断流是否支持 mark() 操作。并非所有 Reader 都支持<br />（如 BufferedReader 支持，但 FileReader 不一定支持）。 |
| `void reset()`                            | 重置流。将读取位置恢复到最近一次 mark() 标记的位置。                                                           |
| `void close()`                            | 关闭流并释放资源。关闭后调用读取方法会抛出 IOException。                                                       |

### Writer 常用方法

| 方法                                          | 功能说明                                                                     |
| --------------------------------------------- | ---------------------------------------------------------------------------- |
| `void write(int c)`                         | 写入单个字符。参数c是字符的Unicode编码（如传入65则写入'A'）。                |
| `void write(String str)`                    | 直接写入字符串。这是Writer特有的便捷方法，无需手动转换成数组。               |
| `void write(char[] cbuf)`                   | 写入字符数组。将整个数组的内容写入流中。                                     |
| `void write(char[] cbuf, int off, int len)` | 写入字符数组的一部分。从数组的off索引开始，连续写入len个字符。               |
| `void flush()`                              | 刷新缓冲区。将内存缓冲区中暂存的数据强制推送到目的地（如硬盘），但不关闭流。 |
| `void close()`                              | 关闭流。在关闭前会自动调用一次flush()，并释放系统资源。关闭后不能再写入。    |

### BufferedReader 方法

| 方法                                    | 功能说明                                                      |
| --------------------------------------- | ------------------------------------------------------------- |
| `BufferedReader(Reader in)`           | 带缓冲区的字符输入流                                          |
| `BufferedReader(Reader in, int size)` | 带缓冲区大小的字符输入流                                      |
| `String readLine()`                   | 读取一行，会丢弃末尾的换行符<br />读到末尾（EOF）时，返回null |
| Reader的其他方法                        |                                                               |

### BufferedWriter 方法

| 方法                                     | 功能说明                 |
| ---------------------------------------- | ------------------------ |
| `BufferedWriter(Writer out)`           | 带缓冲区的字符输出流     |
| `BufferedWriter(Writer out, int size)` | 带缓冲区大小的字符输出流 |
| `void newLine()`                       | 写入回车换行符           |
| Writer的其他方法                         |                          |

### SequenceInputStream

`SequenceInputStream` 是 `InputStream` 的直接子类，可以将多个输入流顺序连接在一起，形成单一的输入数据流，一个输入流读取完数据关闭后，自动切换到下一个输入流。

| 构造方法                                                | 功能     |
| ------------------------------------------------------- | -------- |
| `SequenceInputStream(Enumeration e)`                  | 有多个流 |
| `SequenceInputStream(InputStream s1, InputStream s2)` | 有2个流  |

### 管道流

管道流是Java中用于在不同线程之间进行通信的机制。它像一根水管，让数据从一个线程（生产者）流入管道（`PipedOutputStream`），另一个线程（消费者）从管道取出数据，即数据流出管道（`PipedInputStream`）。在**多线程环境**中使用。不能在同一个线程使用发送端和接收端，否则容易**死锁**。对于 **生产者** ：它需要将数据 **发送到管道里** 。从生产者的代码来看，数据是**流出**自己的程序，进入管道，所以应该使用 `PipedOutputStream` ，对于 **消费者** ：它需要从管道中 **接收数据** 。从消费者的代码来看，数据是**流入**自己的程序，所以应该使用 `PipedInputStream` 。

- `PipedOutputStream`（管道输出流）是发送端（数据源）。线程 A 将数据写入该流。
- `PipedInputStream`（管道输入流）是接收端（目的地）。线程 B 从该流中读取数据。
- 生产者-消费者模型：输出流 `write()` 数据时，数据被放入缓冲区。输入流 `read()` 数据时，从缓冲区取出数据。
- 阻塞机制：如果缓冲区满了，输出线程会阻塞。如果缓冲区空了，输入线程会阻塞。
- 在使用之前，输入流和输出流必须物理连接，否则会抛出 `IOException`。
- 连接方式 (两种等效)：
  - 构造函数连接：`new PipedInputStream(outputStream);`
  - `connect()` 方法：`inputStream.connect(outputStream);`

#### PipedInputStream 构造方法

| 构造方法                                                  | 功能说明                                 |
| --------------------------------------------------------- | ---------------------------------------- |
| `PipedInputStream()`                                    | 创建一个尚未连接到发送端的管道输入流     |
| `PipedInputStream(PipedOutputStream src)`               | 创建一个连接到src的管道输入流            |
| `PipedInputStream(PipedOutputStream src, int pipeSize)` | 带有管道大小的管道输入流，并连接到发送端 |

#### PipedInputStream 常用方法

| 方法                                    | 功能说明                     |
| --------------------------------------- | ---------------------------- |
| `void connect(PipedOutputStream src)` | 将接收端管道连接到发送端管道 |
| 从 `InputStream` 继承的方法           |                              |

#### PipedOutputStream 构造方法

| 构造方法                                    | 功能说明                             |
| ------------------------------------------- | ------------------------------------ |
| `PipedOutputStream()`                     | 创建一个尚未连接到接收端的管道输出流 |
| `PipedOutputStream(PipedInputStream src)` | 创建一个连接到src的管道输出流        |

#### PipedOutputStream 常用方法

| 方法                                   | 功能说明                     |
| -------------------------------------- | ---------------------------- |
| `void connect(PipedInputStream snk)` | 将发送端管道连接到接收端管道 |
| `void flush()`                       | 刷新缓冲区并全部写出         |

```java
import java.io.*; 
public class PipeWriteTest { 
    public static void main(String[] args) throws IOException { 
        PipedOutputStream out = new PipedOutputStream(); 
        PipedInputStream in = new PipedInputStream(out);
        byte[] data = {10, 20, 30, 40, 50}; 
        out.write(data, 1, 3); // 从数组 data 的索引 1 开始，写入 3 个字节 
        int firstByte = in.read(); 
        System.out.println(firstByte); // 20
    } 
}

import java.io.*;
public class PipedStreamExample {
    public static void main(String[] args) throws IOException {
        // 创建管道流
        PipedOutputStream output = new PipedOutputStream();
        PipedInputStream input = new PipedInputStream(output); // 连接
        // 生产者线程
        Thread producer = new Thread(() -> {
            try (output) {
                for (int i = 1; i <= 5; i++) {
                    String data = "Message " + i;
                    output.write(data.getBytes());
                    output.flush();
                    System.out.println("[Producer] 发送: " + data);
                    Thread.sleep(500); // 模拟生产间隔
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
        // 消费者线程
        Thread consumer = new Thread(() -> {
            try (input) {
                byte[] buffer = new byte[1024];
                int len;
                while ((len = input.read(buffer)) != -1) {
                    String received = new String(buffer, 0, len);
                    System.out.println("[Consumer] 接收: " + received);
                }
            } catch (IOException e) {
                // 当生产者关闭输出流时，read() 会返回 -1，正常退出
                System.out.println("[Consumer] 管道关闭，消费结束");
            }
        });
        producer.start();
        consumer.start();
    }
}
```

## 序列化和反序列化

必须实现 `java.io.Serializable` 和 `java.io.Externalizable` 这两个接口。

```java
// 序列化
// 实现 Serializable 接口 
class MyClass implements Serializable { }
// 1. 找出口（节点流）：确定数据流向哪里 
FileOutputStream fileOut = new FileOutputStream("data.ser"); 
// 2. 套外壳（处理流）：建立对象转换机制 
ObjectOutputStream out = new ObjectOutputStream(fileOut); 
// 3. 动真格（序列化）：将对象转为字节并发出 
out.writeObject(new MyClass()); 
// 完工：关闭流并释放资源
out.close(); 

// 反序列化
// 1. 找来源（节点流） 
FileInputStream fileIn = new FileInputStream("object.ser"); 
// 2. 套外壳（处理流）：
ObjectInputStream in = new ObjectInputStream(fileIn); 
// 3. 还原对象：从流中读取并强转回原类型 
MyClass obj2 = (MyClass) in.readObject(); 
// 4. 关闭流 
in.close(); 
```

- 子类可序列化，父类也应该可序列化。
- 序列化子类时，系统会自动连带序列化所有父类对象。反序列化时，系统会同时恢复子类、父类及它们之间的关联。创建子类实例时，系统已隐式建立了父类实例的关联。如果父类不可序列化：反序列化时，父类的属性会丢失或被迫重置（调用无参构造）。**编译不会报错，但序列化时可能抛出异常**。
- 如果类 A 包含类 B 的引用，那么类 B 也必须实现 `Serializable`。否则父级对象在序列化时会抛出异常。
- 序列化编号算法 (Unique ID)：JVM 为每个在磁盘/流中保存的对象分配一个序列化编号。初次序列化时，将对象转换为字节序列并输出。再次序列化时仅输出之前分配的编号，不再重复转换。优点：节省空间，避免循环引用导致的死循环。

## 文件操作：java.io.File 类

### 构造方法

- `File(String pathname)`：支持相对路径（如 `src/config.xml`）。`File f1 = new File("/path/to/file.txt");`
- `File(String parent, String child)`：将路径拆分为父级和子级。父级可以是目录路径，子级可以是文件名或子路径。`File f2 = new File("/parent/directory", "file.txt");`
- `File(File parent, String child)`：先有一个父级 `File` 对象，再在其下寻找子文件。`File parentDir = new File("/parent/directory");``File f3 = new File(parentDir, "file.txt");`
- `File(URI uri)`：通过统一资源标识符创建。
  `URI uri = URI.create("file:///path/to/file.txt");`
  `File f4 = new File(uri);`

### 属性操作 vs 内容访问

- 操作限制：`File` 实例只能操作文件属性（如：删除、重命名、判断是否存在、获取大小等）。
- 内容访问：它不能直接读写文件内容。若需读写，必须配合 I/O 流使用。
- 双重身份：一个 `File` 对象既可以代表一个文件，也可以代表一个目录（文件夹）。

### File 类的“内存映射”特性

- 构造期（内存级）：`new File()` 只是在内存中声明一个路径字符串的包装对象。当你写 `File file = new File("C:/test.txt");` 时，在内存中：只是创建了一个包含字符串 `"C:/test.txt"` 的 Java 对象。不看硬盘：无论这个路径在硬盘上是否存在，或者路径格式写得对不对，程序都不会报错。`File` 对象是逻辑上的路径名，物理上的文件是否存在，需要用 `exists()` 检查。
- 执行期（硬盘级）：只有调用特定方法时，才会与物理硬盘交互。
  创建类：`createNewFile()`, `mkdir()`
  检测类：`exists()`, `isFile()`, `isDirectory()`
  操作类：`delete()`, `renameTo()`

```java
File dir = new File("D:/data"); 
File file = new File(dir, "info.txt");
// 如果D:/data目录不存在，创建file对象时不会抛出异常，只是逻辑对象。
```

### File 类常用方法

| 分类               | 方法及功能简述                                                         |
| ------------------ | ---------------------------------------------------------------------- |
| 访问文件名相关方法 | `String getName()` 返回文件或目录的名称（不含路径）                  |
|                    | `String getPath()` 返回构造File对象时的路径字符串                    |
|                    | `File getAbsoluteFile()` 返回绝对路径对应的File对象                  |
|                    | `String getAbsolutePath()` 返回绝对路径字符串                        |
|                    | `boolean renameTo(File dest)` 重命名文件或目录（需目标路径）         |
| 文件检测相关方法   | `boolean exists()` 判断文件或目录是否存在                            |
|                    | `boolean canWrite()` 判断文件或目录是否可写                          |
|                    | `boolean canRead()` 判断文件或目录是否可读                           |
|                    | `boolean isFile()` 判断是否为普通文件                                |
|                    | `boolean isDirectory()` 判断是否为目录                               |
|                    | `boolean isAbsolute()` 判断路径是否为绝对路径                        |
| 获取常规文件信息   | `long lastModified()` 返回文件最后修改时间（毫秒数）                 |
|                    | `long length()` 返回文件内容的字节长度，对空文件返回0                |
| 目录操作相关方法   | `boolean mkdir()` 创建单级目录                                       |
|                    | `String[] list()` 返回目录中所有文件和子目录的名称数组               |
|                    | `File[] listFiles()` 返回目录中所有文件和子目录的File对象数组        |
|                    | `static File[] listRoots()` 列出系统所有根路径（如Windows的C: D:等） |
| 文件操作相关方法   | `boolean createNewFile()` 创建新文件（若不存在）                     |
|                    | `boolean delete()` 删除文件或空目录                                  |
|                    | `static File createTempFile` 在默认临时目录创建临时文件              |
|                    | `static File createTempFile` 在指定目录创建临时文件                  |
|                    | `void deleteOnExit()` 请求在JVM退出时删除文件或目录                  |

### 文件过滤器

Java 通过 `FilenameFilter` 接口过滤文件。该接口里包含了一个 `accept(File dir, String name)` 方法，`accept` 方法将依次对指定 `File` 的所有子目录或者文件进行迭代，如果该方法返回 `true`，则 `list` 方法会列出该子目录或者子文件。`File` 的 `list(FilenameFilter)` 方法接受 `FilenameFilter` 参数，通过该参数可以只列出符合条件的文件。

```java
File dir = new File("C:/myProject"); // 指定目录 
// 创建过滤器 
FilenameFilter filter = new FilenameFilter() { 
    @Override 
    public boolean accept(File dir, String name) {
        // 逻辑：如果文件名以 .java 结尾，就返回true,否则返回false 
        return name.endsWith(".java");
    }
}; 
// 传入过滤器，获取结果 
String[] fileList = dir.list(filter);
```

## RandomAccessFile（随机访问文件类）

包含一个文件指针，可以随机读写文件内容，即可以直接跳转到文件的任意地方来读写数据。

- 直接父类：`java.lang.Object`，并实现了 `DataInput` 和 `DataOutput` 接口。
- 特殊性：它是 Java IO 体系中极少数不继承 `InputStream` 或 `OutputStream` 的类。
- 设计逻辑：因同时具备“读”和“写”的功能，无法简单地归类为纯输入或纯输出流。

### RandomAccessFile 常用方法

- `read(byte[], offset, len)`, `readXxx()`, `readLine()`
- `write(byte[], int, offset, len)`, `writeXxx()`, `writeBytes(byte[])`
- `writeChars(String)`
- `seek(long pos)` 用于设置文件指针的偏移量（单位：字节），`seek(0)` 将文件指针移动到文件最开头。

### RandomAccessFile 构造器

`RandomAccessFile(String fileName, String mode)`
`RandomAccessFile(File fileName, String mode)`

| mode 值   | 含义                                                                           | 说明                                                                                                                               |
| --------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| `"r"`   | **只读模式** (Read-only)                                                 | 只能读取文件数据。如果试图执行任何写入操作，程序都会抛出 `IOException` 异常。                                                    |
| `"rw"`  | **读写模式** (Read-write)                                                | 可以同时进行读取和写入。如果打开的文件不存在，程序会自动尝试创建它。<br />不会删除原有内容，文件指针初始位置为 **0**。       |
| `"rws"` | **读写 + 同步更新文件和元数据** <br />(Read-write, sync file & metadata) | 在 `"rw"`<br /> 的基础上，**每一次**写入文件的内容或修改文件的元数据（如修改时间等），<br />都会立刻同步到底层存储设备上。 |
| `"rwd"` | **读写 + 同步更新文件内容** (Read-write, sync file content)              | 在 `"rw"` 的基础上，**每一次**写入文件的内容都会立刻同步到底层存储设备上，<br />但元数据的更新不一定立即同步。             |

### RandomAccessFile 常用方法分类

| 分类               | 方法                                       | 简述                        |
| ------------------ | ------------------------------------------ | --------------------------- |
| **指针操作** | `long getFilePointer()`                  | 返回当前指针位置            |
|                    | `void seek(long pos)`                    | 将指针移动到指定位置        |
|                    | `long length()`                          | 返回文件长度                |
|                    | `void setLength(long newLength)`         | 设置文件长度                |
| **读方法**   | `int read()`                             | 读取一个字节                |
|                    | `int read(byte[] b)`                     | 读取字节到数组              |
|                    | `int read(byte[] b, int off, int len)`   | 读取len个字节到数组指定位置 |
|                    | `void readFully(byte[] b)`               | 读取足够填满数组的字节      |
|                    | `int skipBytes(int n)`                   | 跳过n个字节                 |
|                    | `String readLine()`                      | 读取一行文本（不推荐）      |
|                    | `String readUTF()`                       | 读取UTF-8字符串             |
|                    | `readBoolean/Byte/Char/Double`           | 读取对应基本类型            |
| **写方法**   | `void write(int b)`                      | 写入一个字节                |
|                    | `void write(byte[] b)`                   | 写入字节数组                |
|                    | `void write(byte[] b, int off, int len)` | 写入数组的部分字节          |
|                    | `void writeUTF(String str)`              | 写入UTF-8字符串             |
|                    | `void writeBytes(String s)`              | 写入字符串（低字节）        |
|                    | `void writeChars(String s)`              | 写入字符串（每个字符2字节） |
|                    | `writeBoolean/Byte/Char/Double`          | 写入对应基本类型            |
| **其他**     | `void close()`                           | 关闭流                      |
|                    | `FileChannel getChannel()`               | 获取文件通道（NIO）         |

## 线程

线程可以拥有自己的堆栈、程序计数器和局部变量，但不拥有系统资源。它与父进程的其它线程共享该进程所拥有的系统资源和地址空间。系统创建进程需要为该进程重新分配系统资源和地址空间，但创建线程则代价小得多。

### Java创建线程的三种方法

1. 继承 `java.lang.Thread` 类
2. 实现 `java.lang.Runnable` 接口
3. 实现 `java.lang.Callable` 接口

#### 继承 `java.lang.Thread` 类

启动线程必须调用 `start()` 方法。直接调用 `run()` 只属于普通的同步方法调用，不会创建或启动新线程。

```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running");
    }
}
public class Main {
    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start();
    }
}
```

#### 实现 `java.lang.Runnable` 接口

`Runnable` 接口中有一个名为 `run` 的方法。实现 `Runnable` 接口可以避免Java单继承的限制。调用 `start()` 时即调用其中的 `run` 方法。

```java
// 1. 定义任务
class MyTask implements Runnable {
    @Override
    public void run() {
        System.out.println(Thread.currentThread().getName() + " 正在运行");
    }
}
// 2. 装配并启动
public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new MyTask()); 
        thread.start(); // 3. 启动
    }
}
```

#### 实现 `java.lang.Callable` 接口

`Callable<T>` 泛型接口具有 `call()` 方法。可以返回值和声明异常（方法内可以使用 `throws`）。

泛型类 `FutureTask<T>` 实现了泛型接口 `Future<T>` 和 `Runnable` 接口，泛型接口 `Future<T>` 里的 `get()` 方法可以获取返回值（返回值类型为T），通过实现 `Runnable` 接口来可作为 `Thread` 的参数。

用实现 `Callable<T>` 泛型接口的对象做参数创建 `FutureTask<T>` 对象时，`FutureTask<T>` 对象实现的 `run()` 方法会自动调用 `Callable<T>` 泛型接口的 `call()` 方法。

```java
import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;
// 1. 定义带返回值的任务
class MyTask implements Callable<Integer> {
    @Override
    public Integer call() throws Exception {
        return 42; // 支持返回结果和抛出异常
    }
}
public class Main {
    public static void main(String[] args) throws Exception {
        // 2. 包装任务
        FutureTask<Integer> futureTask = new FutureTask<>(new MyTask());
        // 3. 创建线程
        Thread t = new Thread(futureTask);
        t.start(); // 4. 启动线程
        // 5. 获取结果（线程执行完前会阻塞）
        Integer result = futureTask.get(); 
        System.out.println("结果是: " + result);
    }
}
```

### 线程的生命周期

- 新建 -> 就绪：调用 `start()` 方法
- 就绪 -> 运行：获得CPU资源
- 运行 -> 就绪：失去CPU资源，或主动调用 `Thread.yield()`（提示）
- 运行 -> 阻塞：主动调用 `Thread.sleep(long)`（不释放同步锁），使用阻塞式IO方法（`BlockingQueue`, `BlockingDeque`），等待同步监听器（同步锁），等待通知 `wait()`（只能在**synchronized**代码块中调用），主动调用 `join()` / `join(long)` / `join(long, long)` 来插入线程，主动调用 `suspend()`
- 阻塞 -> 就绪：`sleep` 时间到，阻塞式IO方法返回，获得同步监听器，获得通知 `notify()`，插入的线程执行完，`resume()`
- 运行 -> 死亡：发生异常或者错误，`run()` / `call()` 方法执行完毕，主动调用 `stop()`

### Thread 常用方法

| 方法                                               | 功能说明                                                                                                         |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `public static Thread currentThread()`           | 获取当前正在运行的线程                                                                                           |
| `public final String getName()`                  | 返回线程的名字                                                                                                   |
| `public void start()`                            | 启动线程（从新建状态切换到就绪状态）                                                                             |
| `public void run()`                              | 线程执行体                                                                                                       |
| `public final Boolean isAlive()`                 | 如果线程处于就绪、运行、阻塞状态返回 True；<br />如果线程处于新建，或已经结束，则返回 False                      |
| `public void interrupt()`                        | 设置中断状态为 True。对于正在运行的线程不会中断，<br />对于处于阻塞状态的线程，则会抛出 `InterruptedException` |
| `public static boolean isInterrupted()`          | 判断一个线程是否被中断                                                                                           |
| `public final void join()`                       | 暂停当前正在运行的线程，让调用 `join()` 方法的线程先执行                                                       |
| `public final int getPriority()`                 | 返回线程优先级。数字1-10，越大优先级越高。<br />线程的默认优先级为5。新建的线程将继承父线程的优先级              |
| `public final void setPriority(int newPriority)` | 设置线程优先级。`MAX_PRIORITY`：10，`NORM_PRIORITY`：5，`MIN_PRIORITY`：1                                  |
| `public static void sleep(long mills)`           | 设置正在运行的线程的睡眠时间，需要捕获 `InterruptedException`。                                                |
| `public static void yield()`                     | 正在运行的线程主动放弃 CPU 资源，返回到就绪状态                                                                  |

### Daemon（后台/守护/精灵）线程

- JVM的垃圾回收线程是典型的后台线程。
- 如果所有的前台线程都死亡，后台线程会自动死亡。
- 调用 `Thread` 对象的 `setDaemon(true)` 方法可将指定线程设置成后台线程。

### 同步（synchronized）

#### 同步块

将共享资源（公共变量）作为同步监听器（锁）并设置 `synchronized` 块，在线程执行体内使用该同步块。

```java
synchronized(共享对象) {
    // 修改共享资源（公共变量）的代码
}
```

```java
// 1. 共享资源类（公共变量）
class Account {
    int balance = 0; 
}
// 2. 线程任务（丈夫和妻子共享同一个 account 对象）
class DepositTask implements Runnable {
    Account account; // 共享资源
    public void run() { // 线程执行体   
        synchronized (account) {  
            // 修改公共变量的代码
            int next = account.balance + 1000;
            account.balance = next;
            System.out.println(account.balance);  
        } // 走出大括号，自动释放同步监听器
    }
}
public class Main {
    public static void main(String[] args) throws InterruptedException {
        // 1. 创建共享资源对象
        Account account = new Account();
        // 2. 创建两个线程任务（共享同一个 account）
        DepositTask task = new DepositTask();
        task.account = account;  // 传递同一个账户引用
        Thread husband = new Thread(task, "丈夫");
        Thread wife = new Thread(task, "妻子");
        // 3. 启动两个线程
        husband.start();
        wife.start();
        // 4. 等待两个线程执行结束
        husband.join();
        wife.join();
        // 5. 输出最终余额（预期 = 1000 + 1000 = 2000）
        System.out.println("最终余额: " + account.balance);
    }
}
```

#### 同步方法

将某个类的当前对象（共享资源、公共变量）作为同步监听器，将该类内部需要修改共享资源的方法设置为 `synchronized` 方法，在线程体内调用。

```java
public synchronized 返回类型 方法名(形参列表) {
    // 修改共享资源（公共变量）的代码
}
// 等价写法
public 返回类型 方法名(形参列表) {
    synchronized(this) {
        // 修改共享资源（公共变量）的代码
    }
}
```

```java
class Account {
    int balance = 0; // 共享公共变量
    // 写法一：【同步方法】使用 synchronized 修饰方法
    public synchronized void deposit1(int amount) {
        this.balance += amount; 
    }
    // 写法二：【等价写法】普通方法内部套上 synchronized(this)
    public void deposit2(int amount) {
        synchronized(this) {
            this.balance += amount; 
        }
    }
}
public class AccountDemo {
    public static void main(String[] args) throws InterruptedException {
        Account account = new Account();
        int threadCount = 10;          // 线程数量
        int depositsPerThread = 1000;  // 每个线程存款次数
        int amountPerDeposit = 1;      // 每次存款金额
        Thread[] threads = new Thread[threadCount];
        // 创建并启动多个线程，每个线程执行 depositsPerThread 次存款
        for (int i = 0; i < threadCount; i++) {
            threads[i] = new Thread(() -> {
                for (int j = 0; j < depositsPerThread; j++) {
                    account.deposit1(amountPerDeposit); // 调用同步方法
                }
            });
            threads[i].start();
        }
        // 等待所有线程执行完毕
        for (int i = 0; i < threadCount; i++) {
            threads[i].join();
        }
    }
}
```

#### 释放同步监视器的情形

线程会在如下几种情况下释放对同步监视器：

- 同步代码块执行结束
- 同步方法中遇到 `return` 终止了该代码块
- 同步方法中出现了未处理的 `Error` 或 `Exception`
- 程序调用了同步监听器对象的 `wait()` 方法

线程会在如下几种情况下不会释放对同步监视器：

- 调用 `Thread.sleep()` 或 `Thread.yield()` 等方法时
- 调用 `suspend()` 方法时，不会释放同步监听器

## 注解（Annotation）

注解也叫元数据，是程序代码里的特殊标记，这些标记可以在编译、类加载、运行时被读取并执行相应的处理。

注解主要用于告诉编译器要做什么事情，在程序中可对任何程序元素进行注解。

分为基本注解，元注解（元数据注解）和自定义注解。

注解标注在类、方法、字段（变量）、构造方法、参数甚至是包上。程序运行时可以通过反射（Reflection）获取注解的内容。

注解的优势是减少或取代XML配置文件，不依赖XML就能生效。

### 常用注解

| 注解                                                 | 所属包/框架              | 作用说明                                                                                                                                                                                                          |
| ---------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `@Override`                                        | `java.lang`            | 标记方法重写父类或实现接口中的方法；编译器会检查是否正确重写。                                                                                                                                                    |
| `@Deprecated`                                      | `java.lang`            | 标记程序元素（类、方法、字段等）已过时，不建议使用。<br />不会导致编译和运行失败。可以用于标记类、方法、字段（成员变量）、构造方法、参数以及包。                                                                  |
| `@SuppressWarnings`                                | `java.lang`            | 抑制编译器警告，需指定警告类型。如 `@SuppressWarnings("unchecked")` 抑制所有“unchecked”警告                                                                                                                   |
| `@SafeVarargs`                                     | `java.lang`            | 标记构造方法或静态方法中的可变长度参数是类型安全的，抑制堆污染警告。                                                                                                                                              |
| `@FunctionalInterface`                             | `java.lang`            | 标记接口为函数式接口（只有一个抽象方法），编译器会检查（Java 8+）。<br />函数式接口可以包含任意数量的默认方法和静态方法。                                                                                         |
| `@Retention`<br />`@Retention(value = 保存范围)` | `java.lang.annotation` | 元注解，指定注解的保留策略（`SOURCE`、`CLASS`、`RUNTIME`）。<br />`SOURCE`-源码阶段，`CLASS`-编译阶段，`RUNTIME`-运行阶段。<br />`SOURCE`表示注解仅保存在源码中，编译后会丢弃，JVM 运行时无法读取。 |
| `@Target`<br />`@Target(value = 作用范围)`       | `java.lang.annotation` | 元注解，指定注解可应用的 Java 元素类型（方法、字段、类等）。                                                                                                                                                      |
| `@Documented`                                      | `java.lang.annotation` | 元注解，表示该注解应被 javadoc.exe 工具记录。                                                                                                                                                                     |
| `@Inherited`                                       | `java.lang.annotation` | 元注解，允许子类继承父类上的注解。                                                                                                                                                                                |
| `@Repeatable`                                      | `java.lang.annotation` | 元注解，表示注解可在同一位置重复使用（Java 8+）。<br />允许使用多个相同类型的注解来修饰同一程序元素，用于保存多个同类型注解中的成员变量值                                                                         |
| 类型注解                                             |                          | 在能够使用类型的地方添加注解。<br />类型注解可以标注在任何能使用类型的地方，如类型声明、方法返回值、泛型类型等。                                                                                                  |

### 自定义注解

```java
[public] @interface 注解名 {
    数据类型 成员变量名() [default 初始值];
}
```

- `@interface` 是关键字，不是注解。
- 注解和类一样，会被编译为“注解名.class”的字节码文件。
- 成员变量名后面的“()”必不可少。

## 反射（Reflection）

反射是指程序在运行时检查和修改自身结构、行为和属性的能力。它允许在运行时检查类、接口、字段和方法，并执行创建新实例、访问字段值、调用方法和查询注解等操作。

反射的主要目的是在Java程序中提供一种在运行时操作类和对象的方法。

例如：一段程序在运行过程中，接收一个对象作为形参，该对象的编译时类型和运行时类型不一致，但程序又需要调用该对象运行时类中的方法，这就需要引用反射（Reflection）机制，保证在程序运行过程中可以知道任意对象的运行时类型，可以构造任意类的对象，可以调用任意对象的属性和方法。

Java 程序在加载一个类时，会生成一个 `java.lang.Class` 类型的对象，通过该对象可以获得字节码文件中的许多信息。这是反射机制的基础。

### 反射常用功能

| 功能 / 操作  | 说明                                                                             |
| ------------ | -------------------------------------------------------------------------------- |
| 获取名称     | `getName()` 获取全类名，`getSimpleName()` 获取简单类名。                     |
| 获取包与父类 | `getPackage()` 返回包信息，`getSuperclass()` 返回父类 Class 对象。           |
| 获取接口     | `getInterfaces()` 返回该类实现的所有接口数组。                                 |
| 获取属性     | `getFields()` 获取公有属性，`getDeclaredFields()` 获取本类所有属性。         |
| 获取方法     | `getMethods()` 获取公有方法，`getDeclaredMethods()` 获取本类所有方法。       |
| 获取构造器   | `getConstructors()` 获取公有构造，`getDeclaredConstructors()` 获取所有构造。 |
| 创建实例     | 通过构造器的 `newInstance()` 创建对象。                                        |
| 类型判断     | `isInterface()`、`isAnnotation()`、`isArray()` 等判断对象类型。            |
| 权限突破     | 对 Declared 获取的私有成员，需 `setAccessible(true)` 才能访问。                |
| 核心区别     | `get` 系列含父类仅限公有；`getDeclared` 仅限本类但含私有。                   |

```java
import java.lang.reflect.Field;
class User {
    private String name = "Java";
}
public class ReflectTest {
    public static void main(String[] args) throws Exception {
        User user = new User();
        Field field = User.class.getDeclaredField("name");
        field.setAccessible(true); 
        field.set(user, "Reflection");
        System.out.println(field.get(user));
    }
} // Reflection
```

### 获取 Class 对象

- `Class cObj = Class.forName("java.lang.String");`
- `Class<Cylinder> cObj = Cylinder.class;`
- `Class<?> cObj = new Cylinder().getClass();`

`java.lang.reflect` 包中有 `Constructor` 类、`Method` 类、`Field` 类和 `Parameter` 类。其中 `Constructor` 类、`Method` 类由 `Executable` 类派生。

```java
import java.lang.reflect.*;
public class ReflectApp {
    public static void main(String[] args) throws Exception {
        Class<?> clazz = StringBuilder.class;

        // 1. 动态创建实例，String.class表示参数类型
        Constructor<?> c = clazz.getConstructor(String.class);
        Object obj = c.newInstance("Hello");

        // 2. 动态修改属性值
        Field f = clazz.getSuperclass().getDeclaredField("value");
        f.setAccessible(true);
        // 3. 动态调用方法，第一个参数：方法名，第二个参数:参数类型
        Method m = clazz.getMethod("append", String.class);
        m.invoke(obj, " World");
    }
}
```

## 内部类

内部类可以分为非静态内部类和静态内部类。私有内部类只能在外部类内部使用，公有内部类可以在外部类的外部使用。声明方法为 `OuterClass.InnerClass`。

### 非静态内部类

当在非静态内部类的方法内访问某个变量时，先找局部变量（prop），再找内部类的属性（`this.prop`），最后找外部类的属性（`外部类.this.prop`）。初始化语法为 `外部类的实例.new InnerClass(形参列表)`。

### 静态内部类

用 `static` 修饰一个内部类被称为静态内部类。静态内部类是一个普通类，可以包含静态成员，也可以包含非静态成员。

行为类似于顶级类，只是被放在外部类中作为命名空间。

静态内部类不能访问外部类的实例成员，只能访问外部类的类成员。初始化语法为 `new OuterClass.InnerClass(形参列表)`。

```java
class Outer {
    class Inner {}          // 非静态内部类
    static class SInner {}  // 静态内部类
}
public class Test {
    public static void main(String[] args) {
        // 1. 实例化非静态内部类
        Outer.Inner inner = new Outer().new Inner();
        // 2. 实例化静态内部类
        Outer.SInner sinner = new Outer.SInner();
    }
}
```

### 匿名内部类

匿名内部类会生成一个实现接口或者继承抽象类的具体类的实例，编译完成的字节码文件为 `外部类名$编号.class`，可以访问外部类的成员变量和方法。

```java
new 接口名、抽象类名、普通类名(形参列表) {
    // 实现接口或抽象类中的所有抽象方法
    // 定义新的方法
    // 继承父类的方法
    // 重写父类的方法
}
// 对于接口，形参列表为空
// 对于抽象类，提供对应构造方法的形参列表
```

## lambda表达式

```java
([参数类型] 参数名) -> {
    // 方法体
    return 结果;
}
```

- 形参列表：如果形参列表中只有一个参数且不使用var关键字时，形参列表的圆括号也可以省略。
- 形参类型可以使用 `var` 进行局部类型推断。使用 `var` 时必须加小括号。
- 如果代码块只包含一条语句，允许省略代码块的花括号。如果使用花括号，则花括号中必须是语句（有分号）`MathOp op = (var x) -> x * x;``MathOp op = (var x) -> { return x * x;};`
- 如果代码块只有一条语句并且它的值会作为返回值，则 `return` 也可以省略。

```java
@FunctionalInterface
interface MyOp { int process(int a, int b); }
public class LambdaDemo {
    public static void main(String[] args) {
        MyOp add = (x, y) -> x + y;
        execute((MyOp)(m, n) -> m * n);
        /* Java 可以根据方法签名自动推断 Lambda 的类型 execute(MyOp op)，
           传入 (m, n) -> m * n 时，编译器能自动推断为 MyOp 类型
           不需要强制类型转换，所以去掉 (MyOp) 不会报错 */
    }
    static void execute(MyOp op) {
        System.out.println(op.process(5, 4));
    }
}
```

## 方法引用

方法引用提供了一种更简洁的方式来表示只调用单个方法的简单lambda表达式，从而增强了代码的可读性和可维护性。方法引用是Lambda表达式的另外一种表现形式。函数式接口的抽象方法已经在另外一个类中有了实现的方法，可以使用方法引用创建函数式接口的对象。用双冒号运算符“::”简化Lambda表达式。

`java.util.function` 包中包含了常用的函数式接口。

### 方法引用的4种引用方式

- 对象名::实例方法名
- 类名::静态方法名
- 类名::实例方法名
- 类名::new

```java
Consumer<String> con = System.out::println;
Function<Integer, Integer> fun = Math::abs;
Supplier<StringBuilder> sup = StringBuilder::new;
```

## 泛型

泛型提供了编译时类型安全检查机制。

泛型可以用在类、接口和方法上。

泛型的类型参数只能是引用类型，不能是基本类型。

Java 的泛型使用的是“类型擦除（Type Erasure）”机制，在编译后，泛型类型参数会被擦除（替换为其上限类型或Object），类型擦除在定义泛型时即完成。运行时并没有保留具体的类型信息。编译时保留类型信息(形式)，运行时擦除(实质)。调用泛型方法时不需要显式指定类型参数。Java7 引入的菱形语法 `<>` 只能用于右侧的构造方法调用。编译器必须通过左侧声明的明确类型来推导右侧 `<>` 中省略的泛型参数。

### 泛型的定义

- 泛型类：`[修饰符] class 类名<T>`
- 泛型接口：`[public] interface 接口名<T>`
- 泛型方法：`[修饰符] <T> 返回值类型 方法名(参数列表)`。一般来说返回值类型和参数列表至少要有一个用到泛型。

## 容器类

```
- java.lang.Object
  - 实现 Iterable 接口的类（间接）
    - Collection 接口
      - List 接口
        - ArrayList
        - LinkedList
      - Set 接口
        - HashSet
    - Map 接口（不继承 Collection，但与容器体系并列）
      - Hashtable
      - TreeMap
  - 迭代器接口（独立于容器类，用于遍历）
    - Iterator
      - ListIterator
  - 标记接口
    - Serializable
```

### Collection 常用方法

| 方法名                    | 功能说明                                                             |
| ------------------------- | -------------------------------------------------------------------- |
| `boolean hasNext()`     | 向右移动时，如果还有更多元素，则返回 true。                          |
| `Integer next()`        | 返回下一个元素并将光标向右移动。抛出 `NoSuchElementException` 异常 |
| `boolean hasPrevious()` | 向左移动时，如果已经有元素，则返回 true。                            |
| `Integer previous()`    | 返回上一个元素并将光标向左移动。                                     |
| `void add(Integer e)`   | 在当前位置（左边）插入一个元素。                                     |
| `void set(Integer e)`   | 替换 `next()` 或 `previous()` 返回的最后一个元素。               |
| `void remove()`         | 删除 `next()` 或 `previous()` 返回的最后一个元素。               |

### Map 常用方法

| 方法名                                         | 功能说明                                                                          |
| ---------------------------------------------- | --------------------------------------------------------------------------------- |
| `V put(K key, V value)`                      | 将指定的键值对放入映射中。如果键已存在，则替换旧值并返回旧值；否则返回 `null`。 |
| `V get(Object key)`                          | 返回指定键所映射的值；如果映射中不含该键，则返回 `null`。                       |
| `V remove(Object key)`                       | 删除指定键的映射关系，并返回对应的值；如果键不存在，返回 `null`。               |
| `boolean containsKey(Object key)`            | 判断映射中是否包含指定的键。                                                      |
| `boolean containsValue(Object value)`        | 判断映射中是否包含指定的值。                                                      |
| `int size()`                                 | 返回映射中的键值对数量。                                                          |
| `boolean isEmpty()`                          | 判断映射是否为空（不包含任何键值对）。                                            |
| `void clear()`                               | 清空映射中的所有键值对。                                                          |
| `Set<K> keySet()`                            | 返回映射中所有键组成的 `Set` 视图。                                             |
| `Collection<V> values()`                     | 返回映射中所有值组成的 `Collection` 视图。                                      |
| `Set<Map.Entry<K,V>> entrySet()`             | 返回映射中所有键值对（`Entry`）组成的 `Set` 视图。                            |
| `V getOrDefault(Object key, V defaultValue)` | 返回指定键映射的值；如果键不存在，则返回 `defaultValue`（Java 8+）。            |
| `V putIfAbsent(K key, V value)`              | 仅当键尚未映射或映射为 `null` 时，才将键值对放入映射，并返回旧值（Java 8+）。   |
