# chains/code_analyzer.py
from langchain_core.prompts import PromptTemplate
from .base_chain import BaseChain

class CodeAnalyzer(BaseChain):
    def analyze_code_block(self, code: str, language: str = "python"):
        """Analyze a block of code with detailed explanation"""
        prompt = PromptTemplate.from_template(
            """
            ### CODE ({language}):
            {code}
            
            ### INSTRUCTION:
            Analyze this code and provide:
            1. A high-level overview of what the code does
            2. Line-by-line explanation
            3. Key programming concepts used
            4. Potential improvements or best practices
            5. Any security considerations
            
            Format the response in Markdown.
            
            ### ANALYSIS:
            """
        )
        
        result = self.llm.invoke(prompt.format(
            code=code,
            language=language
        ))
        
        return result.content

    def explain_specific_lines(self, code: str, line_numbers: list, context: str = ""):
        """Explain specific lines of code with context"""
        prompt = PromptTemplate.from_template(
            """
            ### CODE CONTEXT:
            {context}
            
            ### CODE LINES TO EXPLAIN:
            {code}
            
            ### INSTRUCTION:
            Explain these specific lines of code, including:
            1. What each line does
            2. Why it's implemented this way
            3. How it fits into the larger context
            4. Any important technical concepts used
            
            Format in clear, concise bullet points.
            
            ### EXPLANATION:
            """
        )
        
        result = self.llm.invoke(prompt.format(
            code=code,
            context=context
        ))
        
        return result.content