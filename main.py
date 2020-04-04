from replanned import user
from replanned import category
from replanned import MVC

if __name__ == '__main__':
    
    user = user.User('Andrzej')
    user.update_points(50)
    model = MVC.Model(user)
    view = MVC.DemoView()
    controller = MVC.DemoController(model, view)
    view.add_controller(controller)

    view.launch('data.json')
