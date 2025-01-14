from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from .base_chain import BaseChain

class DocsAnalyzer(BaseChain):
    def analyze_documentation(self, content: str):
        """
        Analyze technical documentation content.
        """
        prompt = PromptTemplate.from_template(
            """
            ### DOCUMENTATION CONTENT:
            {content}
            
            ### INSTRUCTION:
            Analyze this technical documentation and provide:
            1. A concise summary of the main topics covered
            2. Detailed but simplified explanations for complex sections
            3. Key technical concepts explained in an approachable way
            4. Highlights of important sections
            5. Generate concise notes for future reference
            
            Format the response in Markdown.
            
            ### ANALYSIS:
            """
        )
        
        try:
            response = self.llm.invoke(prompt.format(content=content))
            if hasattr(response, 'content'):
                return response.content  # Handle objects with `content` attribute
            else:
                return response  # Directly return the response if it's already a string
        except Exception as e:
            return f"Error analyzing documentation: {str(e)}"

    def generate_notes(self, content: str):
        """
        Generate simplified notes from documentation.
        """
        prompt = PromptTemplate.from_template(
            """
            ### DOCUMENTATION CONTENT:
            {content}
            
            ### INSTRUCTION:
            Summarize this documentation into concise notes suitable for revision. Include:
            - Key concepts and definitions
            - Important steps and processes
            - Best practices and recommendations
            - Common pitfalls and solutions
            
            Format in Markdown bullet points.
            
            ### NOTES:
            """
        )
        
        try:
            response = self.llm.invoke(prompt.format(content=content))
            if hasattr(response, 'content'):
                return response.content  # Handle objects with `content` attribute
            else:
                return response  # Directly return the response if it's already a string
        except Exception as e:
            return f"Error generating notes: {str(e)}"
