SpringAI

# 第一章 Spring AI简介

在当今这样一个快速发展的技术时代，人工智能（AI）已经成为各行各业的一种标配。而作为一款主流的Java应用开发框架Spring，肯定会紧跟时代的潮流，所以，推出了Spring AI框架。

## 1.1 Spring AI是什么

### 1.1.1 官网描述

* **官网地址**  https://spring.io/projects/spring-ai

![image-20250514153245329](image/image-20250514153245329.png)

![image-20250514154438093](image/image-20250514154438093.png)

* Spring AI是一个AI工程领域的应用程序框架；
* Spring AI 是 AI 工程的应用框架。其目标是将 Spring 生态系统设计原则（如可移植性和模块化设计）应用于 AI 领域，并促进使用 POJO 作为应用程序的构建块到 AI 领域。
* 它的目标是将Spring生态系统的设计原则应用于 AI 领域，比如Spring生态系统的可移植性和模块化设计，并促进使用 POJO 作为应用程序的构建块到 AI 领域；
* Spring AI 的核心是提供了开发 AI 大模型应用所需的基本抽象模型，这些抽象拥有多种实现方式，使得开发者可以用很少的代码改动就能实现组件的轻松替换；
* 简言之，Spring AI 是一个 AI 工程师的应用框架，它提供了一个友好的 API 和开发 AI 应用的抽象，旨在简化 AI 大模型应用的开发工作。

### 1.1.2 发布版本

![image-20250517104954450](image/image-20250517104954450.png)

* 目前Spring AI 推出了一个预览版（PRE）和一个快照版（SNAPSHOT），GA版尚未发布，大家可以提前学习，等GA版发布后再真正用在项目中。

```
SNAPSHOT指的是快照版，会在此版本上持续更新。
PRE指的是预览版，主要提供给开发测试人员找bug，不到修改完善的。
GA指的是 General Availability，意为正式发布的版本，推荐使用（主要是稳定）。
```



## 1.2 Spring AI的主要功能

* 第一、 对主流 AI 大模型供应商提供了支持，比如：OpenAI、DeepSeek、Microsoft、Ollama、Amazon、Google HuggingFace等。
* 第二、 支持AI大模型类型包括：聊天、文本到图像、文本到声音等。
* 第三、 支持主流的Embedding Models（嵌入模型）和向量数据库，比如：Azure Vector Search、Chroma、Milvus、Neo4j、Redis、PineCone、PostgreSQL/PGVector 等。
* 第四、 把 AI 大模型输出映射到简单的 Java 对象（POJOs）上。
* 第五、 支持了函数调用（Function calling）功能。
* 第六、 为数据工程提供 ETL（数据抽取、转换和加载）框架。
* 第七、 支持 Spring Boot 自动配置和快速启动，便于运行 AI 模型和管理向量库。



# 第二章 Spring AI快速入门

## 2.1 准备工作

### 2.1.1 什么是DeepSeek

DeepSeek 是一款由深度求索所开发的 AI 人工智能大模型，其基于深度学习和多模态数据融合技术，采用先进的 Transformer 架构和跨模态协同算法，可实现对复杂文档和图像的自动化解析与结构化信息提取。

依托于最新推出的“深度思考”模式（R1），这款AI大模型在极低成本下实现了与国际顶尖模型ChatGPT-o1相媲美的性能表现，其中文理解与输出能力更是远超ChatGPT、Claude等顶尖模型。再加上极具竞争力的API定价和全面开源的策略，让这款AI大模型成功在国际上火爆出圈

如果说AI是一个广泛的概念，那么DeepSeek就是是AI领域中的一个具体产品。

**DeepSeek的特点**‌：

- ‌**成本**‌：DeepSeek致力于降低AI应用的成本。通过采用先进的技术和独特的模型架构，DeepSeek在保持高性能的同时，显著降低了推理和训练的成本。
- ‌**性能**‌：DeepSeek在性能上表现出色。它使用强化学习技术训练，推理过程中包含大量反思与验证，能够处理更加复杂的数据和任务。在一些benchmark测试中，其性能与OpenAI的模型相当，但推理成本远低于同类产品。
- ‌**功能**‌：DeepSeek擅长处理数学、编程和复杂逻辑推理等任务。它的推理能力源于深度思考特性，推理长度与准确率呈正相关。此外，DeepSeek还支持多模态信息处理，能够应对更加多样化的应用场景。
- ‌**应用领域**‌：DeepSeek在多个领域展现出巨大的应用潜力。无论是在医疗、教育、交通等传统领域，还是在智能制造、智慧城市等新兴领域，DeepSeek都有望发挥重要作用。

综上所述，AI是一个广泛的概念，涵盖了人工智能领域的所有技术和应用。而DeepSeek则是AI领域中的一个具体产品，它在成本、性能、功能和应用领域等方面都有着独特的特点和优势。两者之间的关系可以理解为：DeepSeek是AI领域中的一个具体实现和优秀代表。

**如何使用Java集成DeepSeek：**

DeepSeek 作为一款卓越的国产 AI 模型，越来越多的公司考虑在自己的应用中集成。对于 Java 应用来说，我们可以借助 Spring AI 集成 DeepSeek，非常简单方便！



### 2.1.2 DeepSeek开放平台创建API KEY

* 进入DeepSeek官网 https://www.deepseek.com/  点击右上角的 **API开放平台**

![image-20250306195235004](image/image-20250306195235004.png)

* 进入API开放平台，注册用户

![image-20250306195401240](image/image-20250306195401240.png)

* 创建API key

![image-20250306195507880](image/image-20250306195507880.png)

* 根据自己需要，自行充值

![image-20250306195554534](image/image-20250306195554534.png)

* Spring AI 的 openai starter 本质上是通过 RestTemplate 发请求

![image-20250306195728571](image/image-20250306195728571.png)



## 2.2 创建SpringBoot工程

### 2.2.1 引入依赖

* **SpringAI对于SpringBoot和JDK的版本要求**

![image-20250307140919085](image/image-20250307140919085.png)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.3.8</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>

    <groupId>org.example</groupId>
    <artifactId>springai-deepseek</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <spring-ai.version>1.0.0-M5</spring-ai.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-openai-spring-boot-starter</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.ai</groupId>
                <artifactId>spring-ai-bom</artifactId>
                <version>${spring-ai.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

</project>
```

### 2.2.2 创建配置文件

**application.properties**

```properties
server.port=8899
spring.application.name=spring-ai-deepseek-demo

spring.ai.openai.api-key=sk-139298b9e929496290******
spring.ai.openai.base-url=https://api.deepseek.com
spring.ai.openai.chat.options.model=deepseek-chat
spring.ai.openai.chat.options.temperature=0.7
```

* temperature参数用于控制生成文本的多样性。具体来说：

  ‌值越高‌，生成的文本越多样化，但也可能包含更多的随机性和不可预测的内容。
  ‌值越低‌，生成的文本越接近于确定性的结果，即生成的文本会更加一致和可预测。

### 2.2.3 创建启动类

```java
@SpringBootApplication
public class SpringAiDemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringAiDemoApplication.class, args);
    }

}
```

### 2.2.4 创建Controller

```java
@RestController
public class ChatDeepSeekController {

    @Autowired
    private OpenAiChatModel chatModel;

    @GetMapping("/ai/generate")
    public String generate(@RequestParam(value = "message", defaultValue = "hello")
                           String message) {
        String response = this.chatModel.call(message);
        System.out.println("response : "+response);
        return response;
    }
}
```

### 2.2.5 测试

![image-20250306200808047](image/image-20250306200808047.png)



# 第三章 Spring AI的聊天模型

## 3.1 概述

* Spring AI的聊天模型API为开发者提供了一条便捷通道，能够将强大的AI驱动的聊天完成功能无缝集成到各类应用中。借助预先训练的语言模型，如广为人知的GPT，它能够依据用户输入生成自然流畅、类人化的回复。这一API不仅工作机制高效，而且设计理念极为先进，旨在实现简单易用与高度可移植性，让开发者能以极少的代码改动在不同AI模型间自由切换，充分契合Spring框架一贯秉持的模块化与可互换性原则。



## 3.2 ChatClient接口

**ChatClient 是一个接口，它定义了一个与聊天服务交互的客户端。这个接口主要用于创建聊天客户端对象，设置请求规范，以及发起聊天请求。**

### 3.2.1 实现简单的对话

#### 1 需求

用户输入设置用户消息的内容，通过SpringBoot AI封装的方法向 AI 模型发送请求，以字符串形式返回 AI 模型的响应。

#### 2 编写Controller方法

```java
@RestController
public class ChatDeepSeekController {

    private final ChatClient chatClient;

    public ChatDeepSeekController(ChatClient.Builder chatClientBuilder) {
        this.chatClient = chatClientBuilder.build();
    }

    @GetMapping("/chat")
    public String chat(@RequestParam(value = "msg",defaultValue = "给我讲个笑话")
                           String message) {
        //prompt:提示词
        return this.chatClient.prompt()
                //用户输入的信息
                .user(message)
                //请求大模型
                .call()
                //返回文本
                .content();
    }
}
```

#### 3 测试结果

![image-20250515210014987](image/image-20250515210014987.png)

#### 4 总结

```text
ChatClient 接口提供了构建和配置聊天客户端对象的灵活性，以及发起和处理聊天请求的能力。用户可以通过 ChatClient.Builder 来定制客户端的行为，然后使用 prompt() 和 prompt(Prompt prompt) 方法设置请求规范，最后通过 call() 方法发起聊天请求。
```



### 3.2.2 实现角色预设

#### 1 配置默认角色

```java
@Configuration
public class AIConfig {

    @Bean
    public ChatClient chatClient(ChatClient.Builder builder) {
        return builder.defaultSystem("你是一名老师，你精通Java开发，" +
                "你的名字叫小爱。").build();
    }
}
```

#### 2 编写controller

```java
@RestController
@RequestMapping("/ai")
public class AIController {

    @Autowired
    private ChatClient chatClient;

    @GetMapping("/chat")
    public String chat(@RequestParam(value = "msg") String message) {
        return chatClient.prompt().user(message).call().content();
    }
}
```

### 3.2.3 实现流式响应

#### 1 call和stream的区别

（1）非流式输出 call：等待大模型把回答结果全部生成后输出给用户；

（2）流式输出stream：逐个字符输出，一方面符合大模型生成方式的本质，另一方面当模型推理效率不是很高时，流式输出比起全部生成后再输出大大提高用户体验。

#### 2 编写Controller

```java
@GetMapping(value = "/chat/stream",produces="text/html;charset=UTF-8")
public Flux<String> chatStream(@RequestParam(value = "msg") String message) {
    return chatClient.prompt().user(message).stream().content();
}
```

## 3.3 ChatModel接口

### 3.3.1 概述

ChatModel接口作为核心，定义了与AI模型交互的基本方法。它继承自Model<Prompt, ChatResponse>，提供了两个重载的call方法：

```java
public interface ChatModel extends Model<Prompt, ChatResponse> {
    default String call(String message) {...}
    @Override
    ChatResponse call(Prompt prompt);
}
```

在ChatModel接口中，带有String参数的call()方法简化了实际的使用，避免了更复杂的Prompt和 ChatResponse类的复杂性。但是在实际应用程序中，更常见的是使用ChatResponse call()方法，该方法采用Prompt实例并返回ChatResponse。

我们使用的ChatClient底层是使用ChatModel作为属性的，在初始化ChatClient的时候可以指定ChatModel，这里我们直接看底层源码：

```java
//ChatClient（部分构造器代码）
static ChatClient create(ChatModel chatModel) {
    return create(chatModel, ObservationRegistry.NOOP);
}
```



### 3.3.2 实现简单的对话

```java
@RestController
public class DeepSeekController {

    @Autowired
    private ChatModel chatModel;

    @GetMapping
    public String chat(@RequestParam("msg")String msg) {
        return chatModel.call(msg);
    }

    @GetMapping("/openai")
    public String openai(@RequestParam("msg")String msg) {
        ChatResponse call = chatModel.call(
                new Prompt(
                        msg,
                        OpenAiChatOptions.builder()
                                //可以更换成其他大模型，如Anthropic3ChatOptions亚马逊
                                .model("deepseek-chat")
                                .temperature(0.8)
                                .build()
                )
        );
        return call.getResult().getOutput().getContent();
    }
}
```



### 3.3.3 提示词

* 提示词是引导大模型生成特定输出的输入，提示词的设计和措辞会极大地影响模型的响应结果
* Prompt 提示词是与模型交互的一种输入数据组织方式，本质上是一种复合结构的输入，在 prompt 我们是可以包含多组不同角色（System、User、Aissistant等）的信息。如何管理好 Prompt 是简化 AI 应用开发的关键环节。
* Spring AI 提供了 Prompt Template 提示词模板管理抽象，开发者可以预先定义好模板，并在运行时替换模板中的关键词。在 Spring AI 与大模型交互的过程中，处理提示词首先要创建包含动态内容占位符 {占位符} 的模板，然后，这些占位符会根据用户请求或应用程序中的其他代码进行替换。在提示词模板中，{占位符} 可以用 Map 中的变量动态替换。

```java
@GetMapping("/prompt")
public String prompt(@RequestParam("name")
                         String name,
                     @RequestParam("voice")
                         String voice){
    String userText= """
            给我推荐北京的至少三种美食
            """;
    UserMessage userMessage = new UserMessage(userText);
    String systemText= """
            你是一个美食咨询助手，可以帮助人们查询美食信息。
            你的名字是{name},
            你应该用你的名字和{voice}的饮食习惯回复用户的请求。
            """;
    SystemPromptTemplate systemPromptTemplate = new SystemPromptTemplate(systemText);
    //替换占位符
    Message systemMessage = systemPromptTemplate
            .createMessage(Map.of("name", name, "voice", voice));
    Prompt prompt = new Prompt(List.of(userMessage, systemMessage));
    List<Generation> results = chatModel.call(prompt).getResults();
    return results.stream().map(x->x.getOutput().getContent()).collect(Collectors.joining(""));
}
```



# 第四章 Spring AI的函数调用

## 4.1 概述

* Spring AI 的函数调用（Function Calling）功能允许大语言模型在生成回答时触发预定义的外部函数，从而实现动态数据获取或业务逻辑操作（如查询数据库、调用 API 等）。

* SpringAI 帮我们规范了函数定义、注册等过程，并在发起模型请求之前自动将函数注入到 Prompt 中，而当模型决策在合适的时候去调用某个函数时，Spring AI 完成函数调用动作，最终将函数执行结果与原始问题再一并发送给模型，模型根据新的输入决策下一步动作。这其中涉及与大模型的多次交互过程，一次函数调用就是一次完成的交互过程。
* **函数调用的核心流程**
* 第一步，定义函数：声明可供模型调用的函数（名称、描述、参数结构）。
* 第二步，模型交互：将函数信息与用户输入一起发送给模型，模型决定是否需要调用函数。
* 第三步，执行函数：解析模型的函数调用请求，执行对应的业务逻辑。
* 第四步，返回结果：将函数执行结果返回给模型，生成最终回答。



## 4.2 函数调用实现

### 4.2.1 创建自定义的Function

* 下面CalculatorService类自定义了加法和乘法运算的函数

```java
@Configuration
public class CalculatorService {

    public record AddOperation(int a, int b) {

    }

    public record MulOperation(int m, int n) {

    }

    @Bean
    @Description("加法运算")
    public Function<AddOperation, Integer> addOperation() {
        return request -> {
            return request.a + request.b;
        };
    }

    @Bean
    @Description("乘法运算")
    public Function<MulOperation, Integer> mulOperation() {
        return request -> {
            return request.m * request.n;
        };
    }
}
```

* **总结：**
* Spring AI 使自定义函数这个过程变得简单，只需定义一个返回 java.util.Function 的 @Bean 定义，并在调用 ChatModel 时将 bean 名称作为选项进行注册即可。在底层，Spring 会用适当的适配器代码包装你的函数，以便与 AI 模型进行交互，免去了编写繁琐的代码。

### 4.2.2 编写Controller

```java
    @GetMapping(value = "/chat", produces = MediaType.APPLICATION_STREAM_JSON_VALUE)
    public String ragJsonText(@RequestParam(value = "userMessage") String userMessage){
        return ChatClient.builder(chatModel)
                .build()
                .prompt()
                .system("""
您是算术计算器的代理。
您能够支持加法运算、乘法运算等操作，其余功能将在后续版本中添加，如果用户问的问题不支持请告知详情。
在提供加法运算、乘法运算等操作之前，您必须从用户处获取如下信息：两个数字，运算类型。
请调用自定义函数执行加法运算、乘法运算。
请讲中文。
""")
                .user(userMessage)
                .functions("addOperation", "mulOperation")
                .call()
                .content();
    }
```

* 为了让模型知道并调用你的自定义函数，您需要在 Prompt 请求中启用它，如上述代码，在functions("addOperation", "mulOperation")中告知ChatClient要使用这两个自定义函数。
* 另外指定了System Prompt：要求AI 模型被设定为一个算术计算器代理，能够执行加法和乘法运算，并且要求用户提供两个数字和运算类型。这个提示词内容很关键，如何让AI按照自己的意图去执行，要不断测试提示词内容。

### 4.2.3 测试

![image-20250516003801707](image/image-20250516003801707.png)

# 第五章 Spring AI调用Ollama

## 5.1 下载并安装 Ollama

官网：https://ollama.com/  

### 5.1.1 下载Ollama

Ollama 是一个用于本地化部署和管理大型语言模型（LLM）的工具。它支持多种开源模型（如 LLaMA、Alpaca 等），并提供了简单的 API 接口，方便开发者调用。Ollama可以让你在自己的电脑上运行各种强大的 AI 模型，就像运行普通软件一样简单。

![image-20250306201028630](image/image-20250306201028630.png)

### 5.1.2 安装Ollama

* 模型默认安装在C盘，可以修改安装路径

* 点击环境变量，选择下面新建一个系统环境变量 OLLAMA_MODELS ，然后指定想要安装模型的路径 ，比如   “D:\Deepseek”

![image-20250306201749040](image/image-20250306201749040.png)

* 需要重启 Ollama生效



### 5.1.3 拉取 DeepSeek 模型

**硬件配置建议**

* **GPU选择（根据模型大小灵活调整）：**
  入门配置：NVIDIA显卡（≥8GB显存） → 适合7B/8B模型。
  高性能配置：NVIDIA显卡（≥16GB显存） → 支持14B大模型。
  无独立显卡用户：可使用CPU模式运行（速度约为GPU的20%）。

* **内存要求**：≥16GB（推荐32GB，处理长文本时不易卡顿）
* **存储空间**：≥50GB可用空间（建议SSD硬盘，加快模型加载速度）

* **操作系统**：
  Windows 10/11（21H2及以上版本）。
  macOS Ventura 13.4+。
  Ubuntu 22.04 LTS/24.04 LTS

选择适合自己的版本 https://ollama.com/library/deepseek-r1

![image-20250306201323644](image/image-20250306201323644.png)

以windows为例，根据不同版本，执行不同的命令拉取模型

比如，下载1.5b，执行下面命令

```shell
ollama pull deepseek-r1:1.5b
```



### 5.1.4 启动Ollama服务测试

启动 Ollama 服务，默认会监听 http://localhost:11434

```
ollama run deepseek-r1:1.5b
```

![image-20250306202101617](image/image-20250306202101617.png)



## 5.2 Spring AI代码测试

### 5.2.1 创建SpringBoot工程

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.3.8</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>

    <groupId>org.example</groupId>
    <artifactId>springai-deepseek</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <spring-ai.version>1.0.0-M5</spring-ai.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>

        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-ollama-spring-boot-starter</artifactId>
            <version>1.0.0-SNAPSHOT</version>
        </dependency>
    </dependencies>
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.ai</groupId>
                <artifactId>spring-ai-bom</artifactId>
                <version>${spring-ai.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <!--下载spring-ai相关包需要用到的仓库地址-->
    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
        <repository>
            <id>spring-snapshots</id>
            <name>Spring Snapshots</name>
            <url>https://repo.spring.io/snapshot</url>
            <releases>
                <enabled>false</enabled>
            </releases>
        </repository>
    </repositories>

</project>
```



### 5.2.2 创建配置文件

**application.properties**

```properties
server.port=8899
spring.application.name=spring-ai-deepseek-demo

spring.ai.ollama.base-url=http://localhost:11434
spring.ai.ollama.chat.options.model=deepseek-r1:1.5b
spring.ai.ollama.chat.options.temperature=0.7
```



### 5.2.3 创建启动类

```java
@SpringBootApplication
public class SpringAiDemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringAiDemoApplication.class, args);
    }

}
```



### 5.2.4 创建Controller

```java
@RestController
public class ChatDeepSeekController {

    @Autowired
    private OllamaChatModel ollamaChatModel;

    @GetMapping("/ai/test")
    public String generate(@RequestParam(value = "message", defaultValue = "hello")
                           String message) {
        String response = this.ollamaChatModel.call(message);
        System.out.println("response : "+response);
        return response;
    }
}
```



### 5.2.5 测试

![image-20250306202859451](image/image-20250306202859451.png)



# 第六章 Spring AI Alibaba

## 6.1 概述

* 随着生成式 AI 的快速发展，基于 AI 开发框架构建 AI 应用的诉求迅速增长，涌现出了包括 LangChain、LlamaIndex 等开发框架，但大部分框架只提供了 Python 语言的实现。但这些开发框架对于国内习惯了 Spring 开发范式的 Java 开发者而言，并非十分友好和丝滑。

* 因此，我们基于 Spring AI 发布并快速演进 Spring AI Alibaba，是阿里云通义系列模型及服务在 Java AI 应用开发领域的最佳实践，通过提供一种方便的 API 抽象，帮助 Java 开发者我们加速和简化 Java 智能体应用的开发。同时，提供了完整的开源配套，包括可观测、网关、消息队列、配置中心等。
* Spring AI Alibaba 已完整提供 Model、Prompt、RAG、Tools 等 AI 应用开发所需的必备能力，将兼具提示词模板、函数调用、格式化输出等低层次抽象，以及 RAG、智能体、对话记忆等高层次抽象。



## 6.2 快速入门

### 6.2.1 申请阿里云API Key

* 访问阿里云百炼页面并登录账号 https://www.aliyun.com/product/bailian

![image-20250516020053364](image/image-20250516020053364.png)

* 开通“百炼大模型推理”服务，获取API Key。

![image-20250516020114735](image/image-20250516020114735.png)



![image-20250516020227227](image/image-20250516020227227.png)



![image-20250516020305219](image/image-20250516020305219.png)

### 6.2.2 创建SpringBoot工程

官方文档 https://java2ai.com/docs/1.0.0-M6.1/get-started/?spm=4347728f.13ae80de.0.0.6fe5175cWxPTJZ

![image-20250516022739062](image/image-20250516022739062.png)

* **引入依赖**
* **Spring AI Alibaba 基于 Spring Boot 3.x 开发，因此本地 JDK 版本要求为 17 及以上**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>org.example</groupId>
    <artifactId>deepseek-apringai</artifactId>
    <version>1.0-SNAPSHOT</version>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.5</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <spring-ai.version>1.0.0-M5</spring-ai.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>

        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter</artifactId>
            <version>1.0.0-M5.1</version>
        </dependency>
    </dependencies>
    
    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>
</project>
```

### 6.2.3 编写Controller

```java
@RestController
public class DeepSeekController {

    private static final String DEFAULT_PROMPT = "你是一个博学的智能聊天助手，请根据用户提问回答！";

    @Autowired
    private ChatClient dashScopeChatClient;

    public DeepSeekController(ChatClient.Builder chatClientBuilder) {
        this.dashScopeChatClient = chatClientBuilder
                .defaultSystem(DEFAULT_PROMPT)
                // 实现 Chat Memory 的 Advisor
                // 在使用 Chat Memory 时，需要指定对话 ID，以便 Spring AI 处理上下文。
                .defaultAdvisors(
                        new MessageChatMemoryAdvisor(new InMemoryChatMemory())
                )
                // 实现 Logger 的 Advisor
                .defaultAdvisors(
                        new SimpleLoggerAdvisor()
                )
                // 设置 ChatClient 中 ChatModel 的 Options 参数
                .defaultOptions(
                        DashScopeChatOptions.builder()
                                .withTopP(0.7)
                                .build()
                )
                .build();
    }


    @GetMapping("/simple/chat")
    public String simpleChat(String query) {
        return dashScopeChatClient.prompt(query).call().content();
    }
}
```

### 6.2.4 配置文件

```properties
server.port=8899
spring.application.name=spring-ai-deepseek-demo

spring.ai.dashscope.api-key=sk-026f3ee568f34cc3a237***
```



# 第七章 Spring AI的其他模型

## 7.1 图像模型

### 7.1.1 Image Model API概述

* 在Spring AI框架中，Image Model API旨在为与专注于图像生成的各种AI模型进行交互提供一个简单且可移植的接口，使开发者能够以最小的代码改动切换不同的图像相关模型。这一设计符合Spring模块化和互换性的理念，确保开发者可以快速调整其应用程序以适应不同的图像处理相关的AI能力。

* 此外，通过支持像ImagePrompt这样的辅助类来进行输入封装以及使用ImageResponse来处理输出，图像模型API统一了与致力于图像生成的AI模型之间的通信。它管理请求准备和响应解析的复杂性，为图像生成功能提供直接而简化的API交互。

* Image Model API建立在Spring AI通用模型API之上，提供了特定于图像的抽象和实现。

### 7.1.2 Image Model API接口及相关类

#### 1 ImageModel（图像模型）

 这里展示的是ImageModel接口定义：

```java
@FunctionalInterface
public interface ImageModel extends Model<ImagePrompt, ImageResponse> {
	ImageResponse call(ImagePrompt request);
}
```

#### 2 ImagePrompt（图像提示）

ImagePrompt是一个封装了ImageMessage对象列表及可选模型请求选项的ModelRequest。下面显示的是ImagePrompt类的一个简化版本，省略了构造函数和其他工具方法：

```java
public class ImagePrompt implements ModelRequest<List<ImageMessage>> {
    private final List<ImageMessage> messages;
    private ImageOptions imageModelOptions;
    @Override
    public List<ImageMessage> getInstructions() {...}
	@Override
	public ImageOptions getOptions() {...}
}
```

#### 3 ImageMessage（图像消息）

ImageMessage类封装了用于影响生成图像的文本及其权重。对于支持权重的模型，它们可以是正数或负数。

```java
public class ImageMessage {
	private String text; 
	private Float weight;
    public String getText() {...}
	public Float getWeight() {...}
}
```

#### 4 ImageOptions（图像选项）

表示可以传递给图像生成模型的选项。ImageOptions接口扩展了ModelOptions接口，并用于定义可以传递给AI模型的一些可移植选项。

```java
public interface ImageOptions extends ModelOptions {
	Integer getN();
	String getModel();
	Integer getWidth();
	Integer getHeight();
	String getResponseFormat(); // openai - url or base64 : stability ai byte[] or base64
}
```

#### 5 ImageResponse（图像响应）

持有AI模型的输出，每个ImageGeneration实例包含来自单一提示的可能多个输出结果之一。

```java
public class ImageResponse implements ModelResponse<ImageGeneration> {
	private final ImageResponseMetadata imageResponseMetadata;
	private final List<ImageGeneration> imageGenerations;
	@Override
	public ImageGeneration getResult() {
		// get the first result
	}
	@Override
	public List<ImageGeneration> getResults() {...}
	@Override
	public ImageResponseMetadata getMetadata() {...}
}
```

#### 6 ImageGeneration（图像生成）

最终，ImageGeneration类扩展自ModelResult，代表输出响应及有关此结果的元数据。

```java
public class ImageGeneration implements ModelResult<Image> {
	private ImageGenerationMetadata imageGenerationMetadata;
	private Image image;
    @Override
	public Image getOutput() {...}
	@Override
	public ImageGenerationMetadata getMetadata() {...}
}。
```

### 7.1.3 Spring AI实现生成图像

Spring AI框架的ImageModel API 抽象了应用程序通过模型调用实现“文生图”的交互过程，基本流程：应用程序接收文本，调用模型生成图片。ImageModel 的入参为包装类型ImagePrompt，输出类型为ImageResponse

本示例使用spring ai alibaba开源框架，spring-ai-alibaba-starter AutoConfiguration 默认初始化了 ImageModel 实例，我们可以选择直接注入并使用默认实例。

```java
@Autowired
private DashScopeImageModel imageModel;

@GetMapping
public void getImageabli(@RequestParam(value = "msg",defaultValue = "生成一直小猫")
                           String msg, HttpServletResponse res) {
    ImageResponse response = imageModel.call(
            new ImagePrompt(
                    msg,
                    DashScopeImageOptions.builder()
                         .withModel(DashScopeImageApi.DEFAULT_IMAGE_MODEL)
                         .withN(1)//要生成的图像数。必须介于 1 和 10 之间。
                         .withHeight(1024)//生成的图像的高宽度。
                         .withWidth(1024).build())
    );
	//获取生成图像地址
    String imageUrl = response.getResult().getOutput().getUrl();
    try {
        //使用输出流在浏览器输出
        URL url = URI.create(imageUrl).toURL();
        InputStream in = url.openStream();
        res.setHeader("Content-Type", MediaType.IMAGE_PNG_VALUE);
        res.getOutputStream().write(in.readAllBytes());
        res.getOutputStream().flush();
    }catch (Exception e) {
    }
}
```



## 7.2 语音模型

### 7.2.1 Text-to-Speech API概述

在Spring AI框架中，Text-to-Speech API提供了一个基于OpenAI的TTS（文本转语音）模型的语音端点，

使用户能够：

* 朗读写好的博客文章。

* 生成多种语言的语音音频。

* 使用流媒体实现实时音频输出。

这一功能强大的API让用户可以轻松地将文字内容转化为语音内容，不仅支持多语言转换，还能满足实时语音输出的需求，极大地提升了内容的可访问性和用户的体验感。

### 7.2.2 Spring AI实现文本转语音

* 本示例基于spring ai alibaba开源框架

* SpeechSynthesisModel 类是Spring AI Alibaba框架中用于表示和管理文本转语音模型的核心组件之一。

* DashScopeSpeechSynthesisOptions 类通常用于配置文本转语音（TTS）服务的选项，这个类允许开发者指定一系列参数（比如：语速、音调、音量等）来定制化语音合成的结果，从而满足不同的应用场景需求。

```java
@Autowired
private DashScopeSpeechSynthesisModel speechSynthesisModel;

private static final String TEXT = "床前明月光， 疑是地上霜。 举头望明月， 低头思故乡。";
private static final String FILE_PATH = "src/main/resources/tts";

@GetMapping("/tts")
public void tts() throws IOException {
    // 使用构建器模式创建 DashScopeSpeechSynthesisOptions 实例并设置参数
    DashScopeSpeechSynthesisOptions options = DashScopeSpeechSynthesisOptions.builder()
            .withSpeed(1.0)        // 设置语速
            .withPitch(0.9)         // 设置音调
            .withVolume(60)         // 设置音量
            .build();
    SpeechSynthesisResponse response = speechSynthesisModel.call(new SpeechSynthesisPrompt(TEXT,options));
    File file = new File(FILE_PATH + "/output.mp3");
    try (FileOutputStream fos = new FileOutputStream(file)) {
        ByteBuffer byteBuffer = response.getResult().getOutput().getAudio();
        fos.write(byteBuffer.array());
    } catch (IOException e) {
        throw new IOException(e.getMessage());
    }
}
```



# 第八章 Spring AI实现RAG

## 8.1 概述

### 8.1.1 向量化

* 向量数据库（Vector Database）是一种以数学向量的形式存储数据集合的数据库，通过一个数字列表来表示维度空间中的一个位置。在这里，向量数据库的功能是可以基于相似性搜索进行识别，而不是精准匹配。比如说在使用一个商城系统的向量数据库进行查询的时候，用户输入“北京”，其可能返回的结果会是 “中国、北京、华北、首都、奥运会” 等信息；输入“沈阳”，其返回结果可能会是“东北、辽宁、雪花、重工业”等信息。当然，返回的信息取决于向量数据库中存在的数据。用户可以通过参数的设置来限定返回的情况，进而适配不同的需求。

* 嵌入模型（Embedding Model）和向量数据库（Vector Database/Vector Store）是一对亲密无间的合作伙伴，也是 AI 技术栈中紧密关联的两大核心组件，两者的协同作用构成了现代语义搜索、推荐系统和 RAG（Retrieval Augmented Generation，检索增强生成）等应用的技术基础。

### 8.1.2 RAG

#### 1 RAG的基本概念

​	**RAG**，全称 **Retrieval-Augmented Generation** ，中文叫做**检索增强生成**。RAG是一种结合了检索系统和生成模型的新型技术框架，其主要目的有：

- 利用外部知识库
- 帮助大模型生成**更加准确、有依据、最新的回答**

​	通过使用RAG，解决了传统LLM存在的两个主要问题：

- **知识局限性**：LLM的知识被固定在训练数据中，无法知道最新消息。
- **幻觉现象**：LLM有时候会编造出并不存在的答案。

​	通过检索外部知识，RAG让模型突破了知识局限性，也让LLM（大语言模型）的幻觉现象得到解决。

#### 2 RAG的使用场景

​	RAG技术可以用于多种应用场景，根据不同的知识库与提示词，适配不同的需求。下面是一些常见的典型使用场景

- **企业内部知识问答**
  - 需求：员工需要查询公司规章制度、流程文档、技术手册。
  - RAG方案：
    - 把企业文档库作为检索源。
    - 用户提问时，检索相关文档段落。再由模型总结回答
- **金融/法律领域应用**
  - 需求：解答合规、财税、法律问题，要求答案严谨。
  - RAG方案：
    - 检索法条、案例、内部政策文档。
    - 基于检索到的条款生成规范回答
- **电商/客服智能助理**
  - 需求：自动回答用户关于商品、物流、售后等问题
  - RAG方案
    - 检索商品知识库、FAQ文档
    - 给出准确、即时的答复
- **医疗健康领域**
  - 需求：为患者或医生提供疾病知识、药物信息、医院信息、诊疗方案
  - RAG方案
    - 检索医疗文献、医院文档、指南资料
    - 给出专业、可靠的医学服务

#### 3 RAG工作流程概述	

**第一，用户输入问题**

​	用户在输入窗口输入自己的问题，这一数据被接收，并作为后续处理的查询入口

例如：用户提问

> “我的智能手表出现蓝牙连接问题，怎么办？”

**第二，问题向量化**

​	根据用户初始输入的问题，调用Embedding模型，将问题转换为高维向量，以便于后续的想来那个相似度检索。

```
文本："我的智能手表出现蓝牙连接问题，怎么办？"
→ 向量：[0.123, 0.582, ..., 0.001]
```

**第三，向量数据库检索**

​	系统会连接到一个向量数据库（如FAISS、Milvus、Pinecone、Weaviate）。然后用刚才生成的问题向量，检索知识库中与之最相似的文档片段。

​	当检索的时候，常见的检索参数包括：

- Tok-K ：检索最相关的K条记录
- 相似度阈值：控制检索到内容的相关性

​	最后输出的结果往往是K条知识片段

```
1. "蓝牙连接问题通常可以通过重启设备和重新配对解决。"
2. "如果手表固件版本较旧，请更新到最新版本以兼容蓝牙。"
3. "某些环境下，如电磁干扰，也会导致连接失败。"
```

**第四，构建上下文**

这一阶段需要组织提示词（Prompt），让LLM更好地理解背景信息。

这一部分包括：

- 系统提示词（System Prompt）

  提前告诉LLM需要遵循的行为规范，比如

  ```
  你是一个专业的智能手表客服助理。请基于提供的背景资料，准确回答用户的问题。如果资料中没有明确答案，请如实告诉用户而不是编造。
  ```

  系统提示词可以有效地设定模型角色、控制回答风格、防止幻觉

- 构造最终输入（Final Prompt）

  一般会结合以上内容，按照如下格式进行组织

  ```
  【背景资料】
  1. 蓝牙连接问题通常可以通过重启设备和重新配对解决。
  2. 如果手表固件版本较旧，请更新到最新版本以兼容蓝牙。
  3. 某些环境下，如电磁干扰，也会导致连接失败。
  
  【用户问题】
  我的智能手表出现蓝牙连接问题，怎么办？
  
  【回答要求】
  请结合以上资料，用简洁明了的方式回答用户的问题。如果答案无法直接从资料中找到，请礼貌告知用户。
  ```

**第五，调用LLM**

​	将构造好的Prompt提交给LLM（比如Deepseek、Qwen、GPT-4o、Claude等）

- 模型读取检索到的内容和问题
- 组织自然、连贯、准确的回答

生成结果示例：

> "**您好！** 根据我们的资料，您可以尝试重启智能手表并重新进行蓝牙配对。如果问题仍未解决，请检查手表固件是否为最新版本。如处于高电磁干扰环境，也可能影响连接质量，建议更换使用环境。"

**第六，返回最终回答给用户**

​	最终系统将生成的回答返回前端，展示给用户。

**总结：**

在RAG工作时，其运行流程大致为：

1. 用户输入问题
2. 问题向量化
3. 向量数据库检索
4. 构建上下文（含系统提示词）
5. 携带检索内容，调用大模型进行回答
6. 返回最终答案给用户



## 8.2 Spring AI 实现基本 RAG 流程

### 8.2.1 创建配置类

```java
@Configuration
public class RagConfig {

    @Bean
    ChatClient chatClient(ChatClient.Builder builder) {
        return builder.defaultSystem("你将作为一名Java开发语言的专家，对于用户的使用需求作出解答")
                .build();
    }

    @Bean
    VectorStore vectorStore(EmbeddingModel embeddingModel) {
        SimpleVectorStore simpleVectorStore = SimpleVectorStore.builder(embeddingModel)
                .build();

        // 生成一个说明的文档
        List<Document> documents = List.of(
                new Document("产品说明:名称：Java开发语言\n" +
                        "产品描述：Java是一种面向对象开发语言。\n" +
                        "特性：\n" +
                        "1. 封装\n" +
                        "2. 继承\n" +
                        "3. 多态\n"));
        simpleVectorStore.add(documents);
        return simpleVectorStore;
    }

}
```

* **通过这个配置类，完成以下内容：** 

1、配置 ChatClient 作为 Bean，其中设置系统默认角色为Java开发语言专家， 负责处理用户查询并生成回答向量存储配置。

 2、初始化 SimpleVectorStore，加载Java开发语言说明文档，将文档转换为向量形式存储。

### 8.2.2 编写Controller

```java
@Autowired
private ChatClient dashScopeChatClient;

@Autowired
private VectorStore vectorStore;

@GetMapping(value = "/chat", produces = "text/plain; charset=UTF-8")
public String generation(String userInput) {
    // 发起聊天请求并处理响应
    return dashScopeChatClient.prompt()
            .user(userInput)
            .advisors(new QuestionAnswerAdvisor(vectorStore))
            .call()
            .content();
}
```

* 通过添加 QuestionAnswerAdvisor 并提供对应的向量存储，可以将之前放入的文档作为参考资料，并生成增强回答。

### 8.2.3 测试

![image-20250516024405555](image/image-20250516024405555.png)

# 第九章 Spring AI综合案例

* **智能简历筛选助手**
* 该助手借助 Spring AI 的特性结合人工智能技术，为企业提供快速查看应聘候选人的信息及与候选人岗位的匹配度的服务。

## 9.1 搭建环境

* 创建工程，引入依赖

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>org.example</groupId>
    <artifactId>deepseek-apringai</artifactId>
    <version>1.0-SNAPSHOT</version>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.5</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <spring-ai.version>1.0.0-M5</spring-ai.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>com.alibaba.cloud.ai</groupId>
            <artifactId>spring-ai-alibaba-starter</artifactId>
            <version>1.0.0-M5.1</version>
        </dependency>
    </dependencies>
    
    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>
</project>
```

* 创建配置文件

```properties
server.port=8899
spring.application.name=spring-ai-deepseek-demo
spring.ai.dashscope.api-key=sk-026f3ee568f34cc3a237ea272d****
```



## 9.2 创建RAG 知识库

* 用全部候选人的简历构建一个简历知识库

### 9.2.1 创建txt文本

命名“张三简历.txt”，放到resource目录下

![image-20250516095923962](image/image-20250516095923962.png)

```txt
教育经历
北京大学 软件工程 本科 2005.09 - 2009.06
主修课程：Java语言开发、C语言开发、操作系统、编译原理、计算机网络、算法导论、电商商务、电子基础、高等数学、概率论与统计、离散数学。
工作经验
阿里巴巴有限公司 算法工程师
2009-7-1 - 2015-7-10
拥有五年以上的算法工程师经验，熟悉各种开发语言的使用，比如Java、C++、C#等，熟练使用各种主流深度学习框架，能独立开发出高质量、高性能的算法模型，精通数据结构、算法及机器学习模型的实现与优化，在多个项目中负责算法模型的设计与开发，包括基于深度学习的图像识别、语音识别及自然语言处理等方向。。
小米科技有限公司 算法工程师
2015-8-1 - 2020-3-1
担任小米科技有限公司算法工程师，负责参与开发高性能机器学习算法。在项目中，我使用Python和MATLAB编写了多种算法模型，并且实现了GPU加速计算，使得算法在处理大规模复杂数据时表现优异。
就职于小米科技有限公司，作为算法工程师，全程参与了一款自动驾驶系统的开发。在项目中，我主要通过深度学习、目标检测等技术，实现了车辆识别、道路分割等多项技术难点，使得系统在真实道路环境下表现出了较高的稳定性和可靠性。
在小米科技有限公司，我作为算法工程师负责了一项推荐系统的研发。该系统基于用户行为数据，使用协同过滤和深度学习技术，为用户推荐最优质的内容。在项目中，我优化了多种推荐算法，优化推荐精度达到了90%以上。
```

### 9.2.2 添加配置类

```java
@Bean
VectorStore vectorStore(EmbeddingModel embeddingModel) {
    SimpleVectorStore simpleVectorStore = SimpleVectorStore.builder(embeddingModel)
            .build();
    //1 提取文本内容
    String filePath="张三简历.txt";
    TextReader textReader = new TextReader(filePath);
    textReader.getCustomMetadata().put("filePath",filePath);
    List<Document> documents = textReader.get();
    //2 文本切分段落
    TokenTextSplitter splitter =
            new TokenTextSplitter(1200,
                    350, 5,
                    100, true);
    splitter.apply(documents);
	//3 添加
    simpleVectorStore.add(documents);
    return simpleVectorStore;
}
```

* 通过以上过程，一个简单的 RAG 知识库就创建完成了，使用时直接在向量库中检索即可



## 9.3 创建工具类

### 9.3.1 创建工具

* 创建一个工具（Function），可以用来查询候选人应聘的岗位。

```java
public class RecruitServiceFunction implements Function<RecruitServiceFunction.Request, RecruitServiceFunction.Response> {

    @Override
    public Response apply(Request request) {
        String position="未知";
        if(request.name.contains("张三")){
            position="算法工程师";
        }
        return new Response(position);
    }

    public record Request(String name){ }
    public record Response(String position){ }
}
```

### 9.3.2 添加配置类

```java
@Bean
@Description("某某是否有资格面试")
public Function<RecruitServiceFunction.Request, RecruitServiceFunction.Response> recruitServiceFunction(){
    return new RecruitServiceFunction();
}
```



## 9.4 编写应用的人设

角色与目标：你是一个招聘助手，会针对用户的问题，结合候选人经历，岗位匹配度等专业知识，给用户提供指导。
指导原则：你需要确保给出的建议合理科学，不会对候选人的表现有言论侮辱。
限制：在提供建议时，需要强调在个性建议方面用户仍然需要线下寻求专业咨询。
澄清：在与用户交互过程中，你需要明确回答用户关于招聘方面的问题，对于非招聘方面的问题，你的回应是‘我只是一个招聘助手，不能回答这个问题哦’。
个性化：在回答时，你需要以专业可靠的预期回答，偶尔可以带点幽默感。调节气氛。



## 9.5 编写Controller

将人设、知识库、工具通过 Spring AI 框架串联起了，搭建成应用

```java
@Autowired
private ChatModel chatModel;

@GetMapping("/ai/agent")
public String rag(@RequestParam("query")String query){
    //检索挂载信息
    List<Document> documents = vectorStore.similaritySearch(query);

    //提取相关信息
    String info ="";
    if(documents.size()>0){
        info=documents.get(0).getContent();
    }

    //构造系统 prompt
    String systemPrompt= """
            角色与目标：你是一个招聘助手，会针对用户的问题，结合候选人经历，岗位匹配度等专业知识，给用户提供指导。
            指导原则：你需要确保给出的建议合理科学，不会对候选人的表现有言论侮辱。
            限制：在提供建议时，需要强调在个性建议方面用户仍然需要线下寻求专业咨询。
            澄清：在与用户交互过程中，你需要明确回答用户关于招聘方面的问题，对于非招聘方面的问题，你的回应是‘我只是一个招聘助手，不能回答这个问题哦’。
            个性化：在回答时，你需要以专业可靠的预期回答，偶尔可以带点幽默感。调节气氛。
            给你提供一个数据参考，并且给你调用岗位投递检索公户
            请你跟进数据参考与工具返回结果回复用户的请求。
            """;
    //构造用户 prompt
    String userPrompt= """
            给你提供一些数据参考：{info},请回答我的问题：{query}。
            请你跟进数据参考与工具返回结果回复用户的请求。
            """;
    //构造提示词
    SystemMessage systemMessage = new SystemMessage(systemPrompt);
    PromptTemplate promptTemplate = new PromptTemplate(userPrompt);
    Message userMessage =
            promptTemplate.createMessage(Map.of("info", info, "query", query));
    Prompt prompt = new Prompt(
            List.of(userMessage, systemMessage),
        DashScopeChatOptions.builder().withFunctions(Set.of("recruitServiceFunction")).build()
    );

    List<Generation> results = chatModel.call(prompt).getResults();
    String content = results.stream().map(x -> x.getOutput().getContent()).collect(Collectors.joining());
    return content;
}
```



## 9.6 测试

![image-20250516101400644](image/image-20250516101400644.png)