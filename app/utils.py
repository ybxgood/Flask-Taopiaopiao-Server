from app.ext import model


class BaseModel:
    def save(self):
        try:
            model.session.add(self)
            model.session.commit()
            return 'success'
        except Exception as e:
            return 'error'+str(e)


    def delete(self):
        try:
            model.session.delete(self)
            model.session.commit()
            return 'success'
        except Exception as e:
            return 'error'+str(e)


