import json, os, time

class Template:

    def __init__(self):
        self.root_path = os.path.dirname((os.path.abspath(__file__)))
        self.template = {
            'name': '模板',
            'content': '',
            'createdAt': '',
            'lastEditAt': ''
        }
        self.templates = None
        self.__read()

    def __check_path(self):
        if not os.path.exists(f'{self.root_path}/config'):
            os.mkdir(f'{self.root_path}/config')
        if not os.path.exists(f'{self.root_path}/config/template.json'):
            f = open(f'{self.root_path}/config/template.json', 'w')
            f.write('{}')
            f.close()
            
    def __check_exist(self,name):
        for i in self.templates:
            if i['name'] == name:
                return True
        return False 

    def __read(self):
        self.__check_path()
        
        f = open(f'{self.root_path}/config/template.json', 'r')
        data = f.read()
        self.template = json.loads(data)

    def list(self):
        return [i.name for i in self.templates]

    def get(self, name):
        self.template
    
    def set(self, name):
        pass

    def delete():
        pass 
    
    def save(self):
        self.__check_path()
        
        data = json.dumps(self.templates)
        f = open(f'{self.root_path}/config/template.json', 'w')
        f.write(data)
        f.close()
