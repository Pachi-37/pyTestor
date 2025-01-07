import os.path


class SqlUtils:
    @staticmethod
    def read_sql_file(file_path):
        if file_path is None or not os.path.exists(file_path):
            raise FileNotFoundError

        comment_flag = False
        sql_list = []
        sql_cmd = ""
        with open(file_path, 'r', encoding='utf-8') as file:

            for statement in file:
                # remove start comment and end comment
                statement = statement.strip()
                if statement.startswith("/*"):
                    comment_flag = True
                    continue
                if comment_flag and statement.startswith("*/"):
                    comment_flag = False
                    continue
                if statement.startswith("--"):
                    continue
                if comment_flag or statement == "":
                    continue

                sql_cmd += statement
                if statement.endswith(";"):
                    sql_list.append(sql_cmd)
                    sql_cmd = ""

        return sql_list
