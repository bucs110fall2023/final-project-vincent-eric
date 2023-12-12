import pygame

class SpriteSheet():
	def __init__(self, image, count = 0, width = 0, height = 0):
		self.sheet = pygame.image.load(image)
		self.count = count
		self.width = width
		self.height = height
		self.sprite_width, self.sprite_height = self.sheet.get_size()
		self.frame_width = self.sprite_width/count
		'''
  		Description:
    		Initialization and variables.
      	Arguments:
       		image (str): image file
         	count (int): number of frames in animation, default = 0
          	width (int): width of frame, default = 0
           	height (int): height of frame, default = 0
        Return:
        	None
        '''

	def get_image(self, frame, crop_pos = (0,0), color=None,scale=1):
		image = pygame.Surface((self.frame_width, self.sprite_height)).convert_alpha()
		image.fill((0,0,0,0))
		image.blit(self.sheet, crop_pos, ((frame * self.frame_width),0,  self.frame_width, self.sprite_height))
		image = pygame.transform.scale(image, (self.width*scale, self.height*scale))
		image.convert_alpha()
		if color:
			image.set_colorkey("color")

		return image
            
	def get_images(self, crop_pos =(0,0)):
		image_list = []
		for i in range(self.count):
			image_list.append(self.get_image(i))
		return image_list