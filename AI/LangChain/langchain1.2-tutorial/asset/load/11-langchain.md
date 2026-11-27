# How-to guides

Here you’ll find answers to “How do I….?” types of questions. These guides are *goal-oriented* and *concrete*; they're meant to help you complete a specific task. For conceptual explanations see the [Conceptual guide](https://python.langchain.com/docs/concepts/). For end-to-end walkthroughs see [Tutorials](https://python.langchain.com/docs/tutorials/). For comprehensive descriptions of every class and function see the [API Reference](https://python.langchain.com/api_reference/).

## Installation[](https://python.langchain.com/docs/how_to/#installation)

- [How to: install LangChain packages](https://python.langchain.com/docs/how_to/installation/)
- [How to: use LangChain with different Pydantic versions](https://python.langchain.com/docs/how_to/pydantic_compatibility/)

## Key features[](https://python.langchain.com/docs/how_to/#key-features)

This highlights functionality that is core to using LangChain.

- [How to: return structured data from a model](https://python.langchain.com/docs/how_to/structured_output/)
- [How to: use a model to call tools](https://python.langchain.com/docs/how_to/tool_calling/)
- [How to: stream runnables](https://python.langchain.com/docs/how_to/streaming/)
- [How to: debug your LLM apps](https://python.langchain.com/docs/how_to/debugging/)

## Components[](https://python.langchain.com/docs/how_to/#components)

These are the core building blocks you can use when building applications.

### Chat models[](https://python.langchain.com/docs/how_to/#chat-models)

[Chat Models](https://python.langchain.com/docs/concepts/chat_models/) are newer forms of language models that take messages in and output a message. See [supported integrations](https://python.langchain.com/docs/integrations/chat/) for details on getting started with chat models from a specific provider.

- [How to: do function/tool calling](https://python.langchain.com/docs/how_to/tool_calling/)
- [How to: get models to return structured output](https://python.langchain.com/docs/how_to/structured_output/)
- [How to: cache model responses](https://python.langchain.com/docs/how_to/chat_model_caching/)
- [How to: get log probabilities](https://python.langchain.com/docs/how_to/logprobs/)
- [How to: create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)
- [How to: stream a response back](https://python.langchain.com/docs/how_to/chat_streaming/)
- [How to: track token usage](https://python.langchain.com/docs/how_to/chat_token_usage_tracking/)
- [How to: track response metadata across providers](https://python.langchain.com/docs/how_to/response_metadata/)
- [How to: use chat model to call tools](https://python.langchain.com/docs/how_to/tool_calling/)
- [How to: stream tool calls](https://python.langchain.com/docs/how_to/tool_streaming/)
- [How to: handle rate limits](https://python.langchain.com/docs/how_to/chat_model_rate_limiting/)
- [How to: few shot prompt tool behavior](https://python.langchain.com/docs/how_to/tools_few_shot/)
- [How to: bind model-specific formatted tools](https://python.langchain.com/docs/how_to/tools_model_specific/)
- [How to: force a specific tool call](https://python.langchain.com/docs/how_to/tool_choice/)
- [How to: work with local models](https://python.langchain.com/docs/how_to/local_llms/)
- [How to: init any model in one line](https://python.langchain.com/docs/how_to/chat_models_universal_init/)
- [How to: pass multimodal data directly to models](https://python.langchain.com/docs/how_to/multimodal_inputs/)

### Messages[](https://python.langchain.com/docs/how_to/#messages)

[Messages](https://python.langchain.com/docs/concepts/messages/) are the input and output of chat models. They have some `content` and a `role`, which describes the source of the message.

- [How to: trim messages](https://python.langchain.com/docs/how_to/trim_messages/)
- [How to: filter messages](https://python.langchain.com/docs/how_to/filter_messages/)
- [How to: merge consecutive messages of the same type](https://python.langchain.com/docs/how_to/merge_message_runs/)

### Prompt templates[](https://python.langchain.com/docs/how_to/#prompt-templates)

[Prompt Templates](https://python.langchain.com/docs/concepts/prompt_templates/) are responsible for formatting user input into a format that can be passed to a language model.

- [How to: use few shot examples](https://python.langchain.com/docs/how_to/few_shot_examples/)
- [How to: use few shot examples in chat models](https://python.langchain.com/docs/how_to/few_shot_examples_chat/)
- [How to: partially format prompt templates](https://python.langchain.com/docs/how_to/prompts_partial/)
- [How to: compose prompts together](https://python.langchain.com/docs/how_to/prompts_composition/)
- [How to: use multimodal prompts](https://python.langchain.com/docs/how_to/multimodal_prompts/)

### Example selectors[](https://python.langchain.com/docs/how_to/#example-selectors)

[Example Selectors](https://python.langchain.com/docs/concepts/example_selectors/) are responsible for selecting the correct few shot examples to pass to the prompt.

- [How to: use example selectors](https://python.langchain.com/docs/how_to/example_selectors/)
- [How to: select examples by length](https://python.langchain.com/docs/how_to/example_selectors_length_based/)
- [How to: select examples by semantic similarity](https://python.langchain.com/docs/how_to/example_selectors_similarity/)
- [How to: select examples by semantic ngram overlap](https://python.langchain.com/docs/how_to/example_selectors_ngram/)
- [How to: select examples by maximal marginal relevance](https://python.langchain.com/docs/how_to/example_selectors_mmr/)
- [How to: select examples from LangSmith few-shot datasets](https://python.langchain.com/docs/how_to/example_selectors_langsmith/)

### LLMs[](https://python.langchain.com/docs/how_to/#llms)

What LangChain calls [LLMs](https://python.langchain.com/docs/concepts/text_llms/) are older forms of language models that take a string in and output a string.

- [How to: cache model responses](https://python.langchain.com/docs/how_to/llm_caching/)
- [How to: create a custom LLM class](https://python.langchain.com/docs/how_to/custom_llm/)
- [How to: stream a response back](https://python.langchain.com/docs/how_to/streaming_llm/)
- [How to: track token usage](https://python.langchain.com/docs/how_to/llm_token_usage_tracking/)
- [How to: work with local models](https://python.langchain.com/docs/how_to/local_llms/)

### Output parsers[](https://python.langchain.com/docs/how_to/#output-parsers)

[Output Parsers](https://python.langchain.com/docs/concepts/output_parsers/) are responsible for taking the output of an LLM and parsing into more structured format.

- [How to: parse text from message objects](https://python.langchain.com/docs/how_to/output_parser_string/)
- [How to: use output parsers to parse an LLM response into structured format](https://python.langchain.com/docs/how_to/output_parser_structured/)
- [How to: parse JSON output](https://python.langchain.com/docs/how_to/output_parser_json/)
- [How to: parse XML output](https://python.langchain.com/docs/how_to/output_parser_xml/)
- [How to: parse YAML output](https://python.langchain.com/docs/how_to/output_parser_yaml/)
- [How to: retry when output parsing errors occur](https://python.langchain.com/docs/how_to/output_parser_retry/)
- [How to: try to fix errors in output parsing](https://python.langchain.com/docs/how_to/output_parser_fixing/)
- [How to: write a custom output parser class](https://python.langchain.com/docs/how_to/output_parser_custom/)

### Document loaders[](https://python.langchain.com/docs/how_to/#document-loaders)

[Document Loaders](https://python.langchain.com/docs/concepts/document_loaders/) are responsible for loading documents from a variety of sources.

- [How to: load PDF files](https://python.langchain.com/docs/how_to/document_loader_pdf/)
- [How to: load web pages](https://python.langchain.com/docs/how_to/document_loader_web/)
- [How to: load CSV data](https://python.langchain.com/docs/how_to/document_loader_csv/)
- [How to: load data from a directory](https://python.langchain.com/docs/how_to/document_loader_directory/)
- [How to: load HTML data](https://python.langchain.com/docs/how_to/document_loader_html/)
- [How to: load JSON data](https://python.langchain.com/docs/how_to/document_loader_json/)
- [How to: load Markdown data](https://python.langchain.com/docs/how_to/document_loader_markdown/)
- [How to: load Microsoft Office data](https://python.langchain.com/docs/how_to/document_loader_office_file/)
- [How to: write a custom document loader](https://python.langchain.com/docs/how_to/document_loader_custom/)

### Text splitters[](https://python.langchain.com/docs/how_to/#text-splitters)

[Text Splitters](https://python.langchain.com/docs/concepts/text_splitters/) take a document and split into chunks that can be used for retrieval.

- [How to: recursively split text](https://python.langchain.com/docs/how_to/recursive_text_splitter/)
- [How to: split HTML](https://python.langchain.com/docs/how_to/split_html/)
- [How to: split by character](https://python.langchain.com/docs/how_to/character_text_splitter/)
- [How to: split code](https://python.langchain.com/docs/how_to/code_splitter/)
- [How to: split Markdown by headers](https://python.langchain.com/docs/how_to/markdown_header_metadata_splitter/)
- [How to: recursively split JSON](https://python.langchain.com/docs/how_to/recursive_json_splitter/)
- [How to: split text into semantic chunks](https://python.langchain.com/docs/how_to/semantic-chunker/)
- [How to: split by tokens](https://python.langchain.com/docs/how_to/split_by_token/)

### Embedding models[](https://python.langchain.com/docs/how_to/#embedding-models)

[Embedding Models](https://python.langchain.com/docs/concepts/embedding_models/) take a piece of text and create a numerical representation of it. See [supported integrations](https://python.langchain.com/docs/integrations/text_embedding/) for details on getting started with embedding models from a specific provider.

- [How to: embed text data](https://python.langchain.com/docs/how_to/embed_text/)
- [How to: cache embedding results](https://python.langchain.com/docs/how_to/caching_embeddings/)
- [How to: create a custom embeddings class](https://python.langchain.com/docs/how_to/custom_embeddings/)

### Vector stores[](https://python.langchain.com/docs/how_to/#vector-stores)

[Vector stores](https://python.langchain.com/docs/concepts/vectorstores/) are databases that can efficiently store and retrieve embeddings. See [supported integrations](https://python.langchain.com/docs/integrations/vectorstores/) for details on getting started with vector stores from a specific provider.

- [How to: use a vector store to retrieve data](https://python.langchain.com/docs/how_to/vectorstores/)

### Retrievers[](https://python.langchain.com/docs/how_to/#retrievers)

[Retrievers](https://python.langchain.com/docs/concepts/retrievers/) are responsible for taking a query and returning relevant documents.

- [How to: use a vector store to retrieve data](https://python.langchain.com/docs/how_to/vectorstore_retriever/)
- [How to: generate multiple queries to retrieve data for](https://python.langchain.com/docs/how_to/MultiQueryRetriever/)
- [How to: use contextual compression to compress the data retrieved](https://python.langchain.com/docs/how_to/contextual_compression/)
- [How to: write a custom retriever class](https://python.langchain.com/docs/how_to/custom_retriever/)
- [How to: add similarity scores to retriever results](https://python.langchain.com/docs/how_to/add_scores_retriever/)
- [How to: combine the results from multiple retrievers](https://python.langchain.com/docs/how_to/ensemble_retriever/)
- [How to: reorder retrieved results to mitigate the "lost in the middle" effect](https://python.langchain.com/docs/how_to/long_context_reorder/)
- [How to: generate multiple embeddings per document](https://python.langchain.com/docs/how_to/multi_vector/)
- [How to: retrieve the whole document for a chunk](https://python.langchain.com/docs/how_to/parent_document_retriever/)
- [How to: generate metadata filters](https://python.langchain.com/docs/how_to/self_query/)
- [How to: create a time-weighted retriever](https://python.langchain.com/docs/how_to/time_weighted_vectorstore/)
- [How to: use hybrid vector and keyword retrieval](https://python.langchain.com/docs/how_to/hybrid/)

### Indexing[](https://python.langchain.com/docs/how_to/#indexing)

Indexing is the process of keeping your vectorstore in-sync with the underlying data source.

- [How to: reindex data to keep your vectorstore in-sync with the underlying data source](https://python.langchain.com/docs/how_to/indexing/)

### Tools[](https://python.langchain.com/docs/how_to/#tools)

LangChain [Tools](https://python.langchain.com/docs/concepts/tools/) contain a description of the tool (to pass to the language model) as well as the implementation of the function to call. Refer [here](https://python.langchain.com/docs/integrations/tools/) for a list of pre-built tools.

- [How to: create tools](https://python.langchain.com/docs/how_to/custom_tools/)
- [How to: use built-in tools and toolkits](https://python.langchain.com/docs/how_to/tools_builtin/)
- [How to: use chat models to call tools](https://python.langchain.com/docs/how_to/tool_calling/)
- [How to: pass tool outputs to chat models](https://python.langchain.com/docs/how_to/tool_results_pass_to_model/)
- [How to: pass run time values to tools](https://python.langchain.com/docs/how_to/tool_runtime/)
- [How to: add a human-in-the-loop for tools](https://python.langchain.com/docs/how_to/tools_human/)
- [How to: handle tool errors](https://python.langchain.com/docs/how_to/tools_error/)
- [How to: force models to call a tool](https://python.langchain.com/docs/how_to/tool_choice/)
- [How to: disable parallel tool calling](https://python.langchain.com/docs/how_to/tool_calling_parallel/)
- [How to: access the `RunnableConfig` from a tool](https://python.langchain.com/docs/how_to/tool_configure/)
- [How to: stream events from a tool](https://python.langchain.com/docs/how_to/tool_stream_events/)
- [How to: return artifacts from a tool](https://python.langchain.com/docs/how_to/tool_artifacts/)
- [How to: convert Runnables to tools](https://python.langchain.com/docs/how_to/convert_runnable_to_tool/)
- [How to: add ad-hoc tool calling capability to models](https://python.langchain.com/docs/how_to/tools_prompting/)
- [How to: pass in runtime secrets](https://python.langchain.com/docs/how_to/runnable_runtime_secrets/)

### Multimodal[](https://python.langchain.com/docs/how_to/#multimodal)

- [How to: pass multimodal data directly to models](https://python.langchain.com/docs/how_to/multimodal_inputs/)
- [How to: use multimodal prompts](https://python.langchain.com/docs/how_to/multimodal_prompts/)

### Agents[](https://python.langchain.com/docs/how_to/#agents)

note

For in depth how-to guides for agents, please check out [LangGraph](https://langchain-ai.github.io/langgraph/) documentation.

- [How to: use legacy LangChain Agents (AgentExecutor)](https://python.langchain.com/docs/how_to/agent_executor/)
- [How to: migrate from legacy LangChain agents to LangGraph](https://python.langchain.com/docs/how_to/migrate_agent/)

### Callbacks[](https://python.langchain.com/docs/how_to/#callbacks)

[Callbacks](https://python.langchain.com/docs/concepts/callbacks/) allow you to hook into the various stages of your LLM application's execution.

- [How to: pass in callbacks at runtime](https://python.langchain.com/docs/how_to/callbacks_runtime/)
- [How to: attach callbacks to a module](https://python.langchain.com/docs/how_to/callbacks_attach/)
- [How to: pass callbacks into a module constructor](https://python.langchain.com/docs/how_to/callbacks_constructor/)
- [How to: create custom callback handlers](https://python.langchain.com/docs/how_to/custom_callbacks/)
- [How to: use callbacks in async environments](https://python.langchain.com/docs/how_to/callbacks_async/)
- [How to: dispatch custom callback events](https://python.langchain.com/docs/how_to/callbacks_custom_events/)

### Custom[](https://python.langchain.com/docs/how_to/#custom)

All of LangChain components can easily be extended to support your own versions.

- [How to: create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)
- [How to: create a custom LLM class](https://python.langchain.com/docs/how_to/custom_llm/)
- [How to: create a custom embeddings class](https://python.langchain.com/docs/how_to/custom_embeddings/)
- [How to: write a custom retriever class](https://python.langchain.com/docs/how_to/custom_retriever/)
- [How to: write a custom document loader](https://python.langchain.com/docs/how_to/document_loader_custom/)
- [How to: write a custom output parser class](https://python.langchain.com/docs/how_to/output_parser_custom/)
- [How to: create custom callback handlers](https://python.langchain.com/docs/how_to/custom_callbacks/)
- [How to: define a custom tool](https://python.langchain.com/docs/how_to/custom_tools/)
- [How to: dispatch custom callback events](https://python.langchain.com/docs/how_to/callbacks_custom_events/)

### Serialization[](https://python.langchain.com/docs/how_to/#serialization)

- [How to: save and load LangChain objects](https://python.langchain.com/docs/how_to/serialization/)

## Use cases[](https://python.langchain.com/docs/how_to/#use-cases)

These guides cover use-case specific details.

### Q&A with RAG[](https://python.langchain.com/docs/how_to/#qa-with-rag)

Retrieval Augmented Generation (RAG) is a way to connect LLMs to external sources of data. For a high-level tutorial on RAG, check out [this guide](https://python.langchain.com/docs/tutorials/rag/).

- [How to: add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)
- [How to: stream](https://python.langchain.com/docs/how_to/qa_streaming/)
- [How to: return sources](https://python.langchain.com/docs/how_to/qa_sources/)
- [How to: return citations](https://python.langchain.com/docs/how_to/qa_citations/)
- [How to: do per-user retrieval](https://python.langchain.com/docs/how_to/qa_per_user/)

### Extraction[](https://python.langchain.com/docs/how_to/#extraction)

Extraction is when you use LLMs to extract structured information from unstructured text. For a high level tutorial on extraction, check out [this guide](https://python.langchain.com/docs/tutorials/extraction/).

- [How to: use reference examples](https://python.langchain.com/docs/how_to/extraction_examples/)
- [How to: handle long text](https://python.langchain.com/docs/how_to/extraction_long_text/)
- [How to: do extraction without using function calling](https://python.langchain.com/docs/how_to/extraction_parse/)

### Chatbots[](https://python.langchain.com/docs/how_to/#chatbots)

Chatbots involve using an LLM to have a conversation. For a high-level tutorial on building chatbots, check out [this guide](https://python.langchain.com/docs/tutorials/chatbot/).

- [How to: manage memory](https://python.langchain.com/docs/how_to/chatbots_memory/)
- [How to: do retrieval](https://python.langchain.com/docs/how_to/chatbots_retrieval/)
- [How to: use tools](https://python.langchain.com/docs/how_to/chatbots_tools/)
- [How to: manage large chat history](https://python.langchain.com/docs/how_to/trim_messages/)

### Query analysis[](https://python.langchain.com/docs/how_to/#query-analysis)

Query Analysis is the task of using an LLM to generate a query to send to a retriever. For a high-level tutorial on query analysis, check out [this guide](https://python.langchain.com/docs/tutorials/rag/#query-analysis).

- [How to: add examples to the prompt](https://python.langchain.com/docs/how_to/query_few_shot/)
- [How to: handle cases where no queries are generated](https://python.langchain.com/docs/how_to/query_no_queries/)
- [How to: handle multiple queries](https://python.langchain.com/docs/how_to/query_multiple_queries/)
- [How to: handle multiple retrievers](https://python.langchain.com/docs/how_to/query_multiple_retrievers/)
- [How to: construct filters](https://python.langchain.com/docs/how_to/query_constructing_filters/)
- [How to: deal with high cardinality categorical variables](https://python.langchain.com/docs/how_to/query_high_cardinality/)

### Q&A over SQL + CSV[](https://python.langchain.com/docs/how_to/#qa-over-sql--csv)

You can use LLMs to do question answering over tabular data. For a high-level tutorial, check out [this guide](https://python.langchain.com/docs/tutorials/sql_qa/).

- [How to: use prompting to improve results](https://python.langchain.com/docs/how_to/sql_prompting/)
- [How to: do query validation](https://python.langchain.com/docs/how_to/sql_query_checking/)
- [How to: deal with large databases](https://python.langchain.com/docs/how_to/sql_large_db/)
- [How to: deal with CSV files](https://python.langchain.com/docs/how_to/sql_csv/)

### Q&A over graph databases[](https://python.langchain.com/docs/how_to/#qa-over-graph-databases)

You can use an LLM to do question answering over graph databases. For a high-level tutorial, check out [this guide](https://python.langchain.com/docs/tutorials/graph/).

- [How to: add a semantic layer over the database](https://python.langchain.com/docs/how_to/graph_semantic/)
- [How to: construct knowledge graphs](https://python.langchain.com/docs/how_to/graph_constructing/)

### Summarization[](https://python.langchain.com/docs/how_to/#summarization)

LLMs can summarize and otherwise distill desired information from text, including large volumes of text. For a high-level tutorial, check out [this guide](https://python.langchain.com/docs/tutorials/summarization/).

- [How to: summarize text in a single LLM call](https://python.langchain.com/docs/how_to/summarize_stuff/)
- [How to: summarize text through parallelization](https://python.langchain.com/docs/how_to/summarize_map_reduce/)
- [How to: summarize text through iterative refinement](https://python.langchain.com/docs/how_to/summarize_refine/)

## LangChain Expression Language (LCEL)[](https://python.langchain.com/docs/how_to/#langchain-expression-language-lcel)

Should I use LCEL?

LCEL is an orchestration solution. See our [concepts page](https://python.langchain.com/docs/concepts/lcel/#should-i-use-lcel) for recommendations on when to use LCEL.

[LangChain Expression Language](https://python.langchain.com/docs/concepts/lcel/) is a way to create arbitrary custom chains. It is built on the [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html) protocol.

[**LCEL cheatsheet**](https://python.langchain.com/docs/how_to/lcel_cheatsheet/): For a quick overview of how to use the main LCEL primitives.

[**Migration guide**](https://python.langchain.com/docs/versions/migrating_chains/): For migrating legacy chain abstractions to LCEL.

- [How to: chain runnables](https://python.langchain.com/docs/how_to/sequence/)
- [How to: stream runnables](https://python.langchain.com/docs/how_to/streaming/)
- [How to: invoke runnables in parallel](https://python.langchain.com/docs/how_to/parallel/)
- [How to: add default invocation args to runnables](https://python.langchain.com/docs/how_to/binding/)
- [How to: turn any function into a runnable](https://python.langchain.com/docs/how_to/functions/)
- [How to: pass through inputs from one chain step to the next](https://python.langchain.com/docs/how_to/passthrough/)
- [How to: configure runnable behavior at runtime](https://python.langchain.com/docs/how_to/configure/)
- [How to: add message history (memory) to a chain](https://python.langchain.com/docs/how_to/message_history/)
- [How to: route between sub-chains](https://python.langchain.com/docs/how_to/routing/)
- [How to: create a dynamic (self-constructing) chain](https://python.langchain.com/docs/how_to/dynamic_chain/)
- [How to: inspect runnables](https://python.langchain.com/docs/how_to/inspect/)
- [How to: add fallbacks to a runnable](https://python.langchain.com/docs/how_to/fallbacks/)
- [How to: pass runtime secrets to a runnable](https://python.langchain.com/docs/how_to/runnable_runtime_secrets/)

## [LangGraph](https://langchain-ai.github.io/langgraph)[](https://python.langchain.com/docs/how_to/#langgraph)

LangGraph is an extension of LangChain aimed at building robust and stateful multi-actor applications with LLMs by modeling steps as edges and nodes in a graph.

LangGraph documentation is currently hosted on a separate site. You can peruse [LangGraph how-to guides here](https://langchain-ai.github.io/langgraph/how-tos/).

## [LangSmith](https://docs.smith.langchain.com/)[](https://python.langchain.com/docs/how_to/#langsmith)

LangSmith allows you to closely trace, monitor and evaluate your LLM application. It seamlessly integrates with LangChain and LangGraph, and you can use it to inspect and debug individual steps of your chains and agents as you build.

LangSmith documentation is hosted on a separate site. You can peruse [LangSmith how-to guides here](https://docs.smith.langchain.com/), but we'll highlight a few sections that are particularly relevant to LangChain below:

### Evaluation[](https://python.langchain.com/docs/how_to/#evaluation)



Evaluating performance is a vital part of building LLM-powered applications. LangSmith helps with every step of the process from creating a dataset to defining metrics to running evaluators.

To learn more, check out the [LangSmith evaluation how-to guides](https://docs.smith.langchain.com/how_to_guides#evaluation).

### Tracing[](https://python.langchain.com/docs/how_to/#tracing)



Tracing gives you observability inside your chains and agents, and is vital in diagnosing issues.

- [How to: trace with LangChain](https://docs.smith.langchain.com/how_to_guides/tracing/trace_with_langchain)
- [How to: add metadata and tags to traces](https://docs.smith.langchain.com/how_to_guides/tracing/trace_with_langchain#add-metadata-and-tags-to-traces)

You can see general tracing-related how-tos [in this section of the LangSmith docs](https://docs.smith.langchain.com/how_to_guides/tracing).