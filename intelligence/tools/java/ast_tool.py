import jpype # type: ignore
from jpype import JPackage # type: ignore

class JavaASTTool:
    def __init__(self):
        jpype.startJVM(classpath=['path_to_java_parser_jar'])

    def parse_java_code(self, code: str):
        JavaParser = JPackage('com.github.javaparser').JavaParser
        parsed_code = JavaParser.parse(code)
        
        # Now parsed_code is the AST representation of the code
        return parsed_code

    def get_structure(self, parsed_code):
        # Get all methods and classes from the parsed code
        structure = []
        for method in parsed_code.find_all('MethodDeclaration'):
            structure.append({
                "type": "method",
                "name": method.get_name(),
                "docstring": method.get_javadoc_comment() or "None"
            })
        for clazz in parsed_code.find_all('ClassOrInterfaceDeclaration'):
            structure.append({
                "type": "class",
                "name": clazz.get_name(),
                "docstring": clazz.get_javadoc_comment() or "None"
            })

        return {"structure": structure}
