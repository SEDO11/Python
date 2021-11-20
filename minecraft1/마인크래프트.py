from ursina import *
#플레이어 함수 가져오는 기능
from ursina.prefabs.first_person_controller import FirstPersonController

class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.green
        )
    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position = self.position + mouse.normal)

            if key == 'left mouse down':
                destroy(self)

app = Ursina()
'''
#FPS 수치랑 빨간 버튼 제거
#꼭 app = Ursina() 밑에 적어준다.
window.fps_counter.enabled = False
window.exit_button.visible = False
'''
mapsize = 12

#맵 크기 조정
for z in range(mapsize):
    for x in range(mapsize):
        voxel = Voxel(position = (x, 0, z))

#플레이어 라이브러리 이용
player = FirstPersonController()

app.run()