from loader import db
from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter


class IsCura(BoundFilter):
    async def check(self, message: Message):
        cid = message.from_user.id
        if db.fetchone('SELECT role FROM admins WHERE cid=?', (cid,)) is not None:
            role = db.fetchone('SELECT role FROM admins WHERE cid=?', (cid,))[0]
            if role == 'Курьер' or role == 'Админ':
                return True
