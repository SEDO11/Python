from ursina import *

#물체 설정
class Test_cube(Entity):
     def __init__(self):
         super().__init__(
             model = 'cube',
             color = color.white,
             texture = 'white_cube',
             rotation = Vec3(45,45,45) #x, y, z (3차원)
         )

#class랑 def랑 super를 서로 같은 x축에 쓰면 오류뜸
class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent = scene, #크기 조절 / 이거 없애면 커짐
            model = 'cube',
            texture = 'brick',
            color = color.blue,
            highlight_color = color.red, #버튼에 마우스를 갖다 대면 빨간색으로 바뀜
            pressed_color = color.green #버튼을 누를경우 색깔이 초록색으로 바뀜
    )

#버튼을 눌렀을 경우 해당 문구 출력
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print("button pressed")


#이동 칸 & 속도
move = 4

#조종 
def update():
    if held_keys['a']:
    #물체가 왼쪽으로 이동
       sans.x -= move * time.dt

    if held_keys['d']:
    #물체가 오른쪽으로 이동
       sans.x += move * time.dt

    if held_keys['w']:
    #물체가 위으로 이동
       sans.y += move * time.dt

    if held_keys['s']:
    #물체가 위으로 이동
       sans.y -= move * time.dt
    

app = Ursina()

#모양(quad 2차원 사각형, cube 3차원 육면체), 색깔, 크기, 위치 설정
#test_square = Entity(model = 'quad', color = color.green, scale = (1,4), position = (5,1))

sans_texture = load_texture('sans.jpg')
sans = Entity(model = 'quad', texture = sans_texture, position = (-2, 0))

test_cube = Test_button()

app.run()
