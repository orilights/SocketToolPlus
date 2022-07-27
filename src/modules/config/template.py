import json, os, time
from Global import *


class Template:

    def __init__(self):
        self.init = "{\"data\": []}"
        self.template = {'name': '模板', 'content': '', 'createdAt': '', 'lastEditAt': ''}
        self.templates = []
        self.__read()

    def __check_path(self):
        if not os.path.exists(f'{ROOT_PATH}/config'):
            os.mkdir(f'{ROOT_PATH}/config')
        if not os.path.exists(f'{ROOT_PATH}/config/template.json'):
            f = open(file=f'{ROOT_PATH}/config/template.json', mode='w', encoding=ENCODING_FILE)
            f.write(self.init)
            f.close()

    def __check_exist(self, name):
        for i in self.templates:
            if i['name'] == name:
                return True
        return False

    def __read(self):
        self.__check_path()

        f = open(f'{ROOT_PATH}/config/template.json', 'r', encoding=ENCODING_FILE)
        data = f.read()
        self.templates = json.loads(data)['data']

    def list(self):
        return [i['name'] for i in self.templates]

    def get(self, name) -> str:
        for t in self.templates:
            if t['name'] == name:
                return t['content']
        return ''

    def set(self, name, content):
        exist = False
        for t in self.templates:
            if t['name'] == name:
                exist = True
                t['content'] = content
                t['lastEditAt'] = str(int(time.time()))
                break
        if not exist:
            new = self.template.copy()
            new['name'] = name
            new['content'] = content
            new['createdAt'] = str(int(time.time()))
            new['lastEditAt'] = str(int(time.time()))
            self.templates.append(new)
        self.__save()

    def delete(self, name):
        for t in self.templates:
            if t['name'] == name:
                self.templates.pop(self.templates.index(t))
                break
        self.__save()

    def __save(self):
        self.__check_path()
        tmp = {'data': self.templates}
        data = json.dumps(tmp)
        f = open(f'{ROOT_PATH}/config/template.json', 'w', encoding=ENCODING_FILE)
        f.write(data)
        f.close()
