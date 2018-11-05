from random import random as rand
from pygame import Rect
class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def random():
		angle = 2 * math.pi * rand()
		return Vector(math.sin(angle), math.cos(angle))
	
	def copy(self):
		return Vector(self.x, self.y)
		
	def zero():
		return Vector(0,0)
		
	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)
	
	def __neg__(self):
		return Vector(-self.x, -self.y)
		
	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)
		
	def __mul__(self, other):
		return Vector(self.x * other.x, self.y * other.y)
	
	def __iter__(self):
		yield self.x
		yield self.y

class Animal(pygame.sprite.Sprite):
    
    def __init__(self, image, screen, pos, vel, accel):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = JRect(self.image.get_rect(), self.image)
        self.setCenter(center)
		self.vel = vel
		self.accel = accel
		self.screen = screen
		self.alive = True
        
    def setPos(self, pos):
        self.pos = pos
        self.rect.topleft = (pos.x, pos.y)
    
    def draw(self):
        if self.alive:
			self.move()
			self.screen.blit(self.image, self.coordinates())
			self.time += 1
		else:
			self.screen.blit(self.deadImage, self.coordinates())

    def coordinates(self):
		return tuple(self.pos)
	
	def move(self):
		self.accel = self.moves[self.time]
		self.vel += self.accel
		self.pos += self.pos
	
	def getCenter(self):
        return Vector(self.pos.x + self.rect.width // 2, self.pos.y + self.rect.height // 2)

    def setCenter(self, center):
        self.setPos(Vector(center.x - self.rect.width // 2, center.y - self.rect.height // 2))
        
class JRect(Rect):
    
    def __init__(self, rect, image):
        Rect.__init__(self, rect)
        self.image = image
        
    def colliderect(self, other):
        rect = self.clip(other)
        if rect.width == 0:
            return False
        for y in range(rect.top, rect.bottom):
            for x in range(rect.left, rect.right):
                if self.notTransparent(x,y) and other.notTransparent(x,y):
                    return True
        return False
             
    def notTransparent(self, x, y):
        return self.image.get_at((x-self.left, y-self.top))[3] != 0
		
class Population:
	def __init__(self, size, origin, image, screen):
		self.mice = []
		for x in range(size):
			self.mice.append(Mouse(origin, image, screen))
		self.time = 0
		self.generation = 0
	
	def draw(self):
		for mouse in mice:
			mouse.draw(self.screen)
		time += 1


class Mouse(Animal):
	def __init__(self, origin, image, screen):
		pos = origin
		vel = Vector.zero()
		accel = Vector.zero()
		super().__init__(image, screen, pos, vel, accel)		
		
		