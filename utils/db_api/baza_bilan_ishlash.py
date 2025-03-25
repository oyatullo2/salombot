import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([ f"{item} = ?" for item in parameters])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):


        sql = """
        INSERT INTO myfiles_teacher(id, Name, email, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM myfiles_teacher
        """
        return self.execute(sql, fetchall=True)

    def ozgartirish(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM royxattan WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update(self, ism, tg_id):
        # SQL_EXAMPLE = "UPDATE myfiles_teacher SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE myfiles_royxattan_otish SET ism=? WHERE tg_id=?
        """
        return self.execute(sql, parameters=(ism, tg_id), commit=True)

    def update2(self, telefon, tg_id):
        # SQL_EXAMPLE = "UPDATE myfiles_teacher SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE myfiles_royxattan_otish SET telefon=? WHERE tg_id=?
        """
        return self.execute(sql, parameters=(telefon, tg_id), commit=True)

    def delete_userss(self):
        self.execute("DELETE FROM myfiles_teacher WHERE TRUE", commit=True)

    def tugma_yaratish(self, ism:str):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO myfiles_tugma(ism) VALUES(?)
        """
        self.execute(sql, parameters=(ism,), commit=True)

    def user_qoshish(self,ism: str, fam:str,username:str,tg_id:int):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO foydalanuvchilar(ism,fam,username,tg_id) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(ism,fam,username,tg_id), commit=True)

    def select_all_foydalanuvchilar(self):
        sql = """
        SELECT * FROM bot2  
        """
        return self.execute(sql, fetchall=True)

    def select_maxsulot(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_Maxsulotlar WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def odam_qoshish(self,  ism: str,tg_id = int, fam: str = None, username: str = None):

        sql = """
           INSERT INTO users (ism,fam,username,tg_id) VALUES(?, ?, ?, ?)
           """
        self.execute(sql, parameters=(ism,fam,username,tg_id), commit=True)
    def userlar_soni(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)

    def select_barcha_userlar(self):
        sql = """
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)

    def add_maxsulot(self, ism: str, tel: int,tg_id: int):


        sql = """
        INSERT INTO buyurtma2 (ism, tel, tg_id) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(ism, tel, tg_id), commit=True)

    def korsatish(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM bot2 WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def royxattan_otish(self, ism: str,   tg_id:int,telefon:str=None):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO myfiles_royxattan_otish(ism,telefon,tg_id) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(ism,telefon,tg_id), commit=True)

    def kirish(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_royxattan_otish WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def ozgartirish(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM bot WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)






    def buyurtma_yaratish(self, proekt_nomi:str, proekt_tarifi:str, proekt_narxi:str, kategoriya:str, user_id:int):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO bot2(proekt_nomi,proekt_tarifi,proekt_narxi,kategoriya,user_id) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(proekt_nomi, proekt_tarifi, proekt_narxi, kategoriya,user_id), commit=True)

    def ish_olish(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_ish_berish WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)


    def buyurtma_raqami(self):
        return self.execute("SELECT COUNT(*) FROM bot2;", fetchone=True)

    def filter(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM bot2 WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def filter2(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM bot WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def filter4(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM bot2 WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)
    def filter3(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM bot4 WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)
    def select_zakaz(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = " SELECT * FROM bot2 WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)
    def buyurtma_yaratish2(self, salom:str,user_id:int):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO bot3(salom,user_id) VALUES(?, ?)
        """
        self.execute(sql, parameters=(salom,user_id), commit=True)
    def buyurtma_yaratish3(self, salom:str, user_id:int,foydalanuvchi_id:int,taklif:str):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO bot4(salom,user_id,foydalanuvchi_id,taklif) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(salom,user_id,foydalanuvchi_id,taklif), commit=True)

    def ochirishsh(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = " DELETE  FROM ish_berish WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def royxattan_otish2(self, ismi: str,   tg_id:int, telefon:str=None):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO royxattan(ismi,telefon,tg_id) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(ismi,telefon,tg_id), commit=True)

    def ish_berish(self, ismi: str,   tg_id:int,kategoriya:str,vaqt:int,manzil:str,narxi:int, telefon_Raqami:str):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO myfiles_ish_berish(ismi,telefon_Raqami,tg_id,kategoriya,vaqt,manzil,narxi) VALUES(?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(ismi,telefon_Raqami,tg_id,kategoriya,vaqt,manzil,narxi), commit=True)

    def filter_ish_b(self, **kwargs):
            # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
            sql = "SELECT * FROM myfiles_ish_berish WHERE "
            sql, parameters = self.format_args(sql, kwargs)

            return self.execute(sql, parameters=parameters, fetchall=True)
def logger(statement):
    print(f"""
__________________________________________       
QARA: 
{statement}
__________________________________________
""")

