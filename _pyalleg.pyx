
# WARNING! I do not guarantee the readability of this code.
#  -akx


license="""

PyAlleg - Python wrapper for the Allegro library
================================================
Allegro: http://alleg.sf.net
Python:  http://www.python.org
PyAlleg: http://www.devever.net/akx/pyalleg/

PyAlleg is Copyright (c) 2005 AKX <theakx.tk>

This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.

Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

    1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.
    2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.
    3. This notice may not be removed or altered from any source distribution.
"""

import time

cdef extern from "all.h":
	###################################
	ctypedef struct JOYSTICK_AXIS_INFO:
		int pos
		int d1,d2
		char *name
		
	ctypedef struct JOYSTICK_STICK_INFO:
		int flags
		int num_axis
		char *name

	ctypedef struct JOYSTICK_BUTTON_INFO:
		int b
		char *name
		
	ctypedef struct JOYSTICK_INFO:
		int flags
		int num_sticks
		int num_buttons
		JOYSTICK_STICK_INFO stick[5]
		JOYSTICK_BUTTON_INFO button[32]	
		
	ctypedef struct RGB:
		unsigned char r
		unsigned char g
		unsigned char b
		unsigned char filler
	
	ctypedef RGB PALETTE[256]
	ctypedef int fixed
	fixed ftofix (double x)
	
	ctypedef struct GFX_MODE:
		int width, height, bpp
		
	ctypedef struct GFX_MODE_LIST:
		int num_modes
		GFX_MODE *mode
		
	ctypedef struct GFX_VTABLE:
		pass
		
	ctypedef struct BITMAP:
		int w, h
		int clip
		int cl, cr, ct, cb
		GFX_VTABLE *vtable
		void *write_bank
		void *read_bank
		void *dat
		unsigned long id
		void *extra
		int x_ofs
		int y_ofs
		int seg
		unsigned char **line
	
	ctypedef struct SAMPLE:
		int bits
		int stereo
		int freq
		int priority
		unsigned long len
		unsigned long loop_start
		unsigned long loop_end
		unsigned long param
		void *data

	ctypedef struct FONT:
		pass

	# Config routines omitted.
	
	char *allegro_id
	char *allegro_error
	int os_type
	int os_version
	int os_revision
	
	void check_cpu()
	char cpu_vendor[]
	int cpu_family
	int cpu_model
	int cpu_capabilities
	
	int allegro_init()
	void allegro_exit()
	void set_window_title(char *name)
	int desktop_color_depth ()
	int get_desktop_resolution (int *width, int *height)
	
	void yield_timeslice ()
	
	#####################################
	
	int install_mouse ()
	void remove_mouse ()
	int mouse_x
	int mouse_y
	int mouse_z
	int mouse_b
	void show_mouse(BITMAP *bmp)
	void scare_mouse()
	void unscare_mouse()
	void position_mouse(int x,int y)
	void position_mouse_z(int z)
	void set_mouse_range (int x1,int y1,int x2,int y2)
	void set_mouse_speed (int xspeed, int yspeed)
	void set_mouse_sprite (BITMAP *sprite)
	void select_mouse_cursor (int cursor)
	int show_os_cursor (int cursor)
	void get_mouse_mickeys (int *mickeyx, int *mickeyy)
	
	# Timers are omitted, except for rest.
	void rest(int tyme)
	
	#################################
	
	int install_keyboard ()
	void remove_keyboard ()
	char key[]
	int key_shifts
	int keypressed ()
	int readkey ()
	void clear_keybuf ()
	
	#################################
	
	
		
	JOYSTICK_INFO joy[]
	int num_joysticks
	
	int install_joystick (int type)
	void remove_joystick ()
	int poll_joystick ()
	
	########################
	
	
	
	
	BITMAP *screen
	
	int SCREEN_W,SCREEN_H,VIRTUAL_W,VIRTUAL_H
	
	GFX_MODE_LIST *get_gfx_mode_list (int card)
	void destroy_gfx_mode_list(GFX_MODE_LIST *gfx_mode_list)
	void set_color_depth (int depth)
	int get_color_depth ()
	void request_refresh_rate (int rate)
	int get_refresh_rate ()
	int set_gfx_mode (int card, int w, int h, int v_w, int v_h)
	int scroll_screen (int x, int y)
	BITMAP *create_bitmap (int width, int height)
	BITMAP *create_bitmap_ex (int color_depth, int width, int height)
	BITMAP *create_sub_bitmap (BITMAP *parent, int x, int y, int width, int height)
	BITMAP *create_video_bitmap (int width, int height)
	BITMAP *create_system_bitmap (int width, int height)
	BITMAP *load_bitmap (char *filename, RGB *pal)
	int save_bitmap (char *filename, BITMAP *bmp, RGB *pal)
	void destroy_bitmap (BITMAP *bitmap)
	void set_clip_rect (BITMAP *bitmap, int x1, int y_1, int x2, int y2)
	void clear_bitmap (BITMAP *bitmap)
	void clear_to_color (BITMAP *bitmap, int color)
	void vsync ()
	int is_same_bitmap (BITMAP *bmp1, BITMAP *bmp2)
	int is_linear_bitmap (BITMAP *bmp)
	int is_planar_bitmap (BITMAP *bmp)
	int is_memory_bitmap (BITMAP *bmp)
	int is_screen_bitmap (BITMAP *bmp)
	int is_video_bitmap (BITMAP *bmp)
	int is_system_bitmap (BITMAP *bmp)
	int is_sub_bitmap (BITMAP *bmp)
	void acquire_bitmap (BITMAP *bmp)
	void release_bitmap (BITMAP *bmp)
	void acquire_screen ()
	void release_screen ()
	int is_inside_bitmap (BITMAP *bmp, int x, int y, int clip) 
	
	#PALETTE black_palette
	#PALETTE desktop_palette
	#PALETTE default_palette
	#void set_color (int idx, RGB *p)
	#void set_palette (PALETTE p)
	#void set_palette_range (PALETTE p, int fr0m, int to, int retracesync)
	#void get_color (int idx, RGB *p)
	#void fade_interpolate (PALETTE source, PALETTE dest, PALETTE output, int pos, int fr0m, int to)
	#void fade_fr0m_range (PALETTE source, PALETTE dest, int speed, int fr0m, int to)
	#void fade_in_range (PALETTE p, int speed, int fr0m, int to)
	#void fade_out_range (int speed, int fr0m, int to)
	#void fade_fr0m (PALETTE source, PALETTE dest, int speed)
	#void fade_in (PALETTE p, int speed)
	#void fade_out (int speed)
	#void generate_332_palette (PALETTE pal)
	#void create_rgb_table (RGB_MAP *table, PALETTE pal, void *callback)
	#void create_light_table (COLOR_MAP *table, PALETTE pal, int r, int g, int b, void *callback)
	#void create_trans_table (COLOR_MAP *table, PALETTE pal, int r, int g, int b, void *callback
	#void create_color_table (COLOR_MAP *table, PALETTE pal, void *blend, void *callback)
	#void create_blender_table (COLOR_MAP *table, PALETTE pal, void *callback)
	void set_alpha_blender ()
	void set_write_alpha_blender ()
	void set_trans_blender (int r, int g, int b, int a)
	void set_add_blender (int r, int g, int b, int a)
	void set_burn_blender (int r, int g, int b, int a)
	void set_color_blender (int r, int g, int b, int a)
	void set_difference_blender (int r, int g, int b, int a)
	void set_dissolve_blender (int r, int g, int b, int a)
	void set_dodge_blender (int r, int g, int b, int a)
	void set_hue_blender (int r, int g, int b, int a)
	void set_invert_blender (int r, int g, int b, int a)
	void set_luminance_blender (int r, int g, int b, int a)
	void set_multiply_blender (int r, int g, int b, int a)
	void set_saturation_blender (int r, int g, int b, int a)
	void set_screen_blender (int r, int g, int b, int a)
	void hsv_to_rgb (float h, float s, float v, int *r, int *g, int *b)
	void rgb_to_hsv (int r, int g, int b, float *h, float *s, float *v)
	int makecol (int r, int g, int b)
	int makeacol (int r, int g, int b, int a)
	int getr (int c)
	int getg (int c)
	int getb (int c)
	int geta (int c)
	void drawing_mode (int mode, BITMAP *pattern, int x_anchor, int y_anchor)
	void xor_mode (int on)
	void solid_mode ()
	
	###############################################
	
	void blit (BITMAP *source, BITMAP *dest, int source_x, int source_y, int dest_x, int dest_y, int width, int height)
	void masked_blit (BITMAP *source, BITMAP *dest, int source_x, int source_y, int dest_x, int dest_y, int width, int height)
	void stretch_blit (BITMAP *s, BITMAP *d, int s_x, int s_y, int s_w, int s_h, int d_x, int d_y, int d_w, int d_h)
	void masked_stretch_blit (BITMAP *s, BITMAP *d, int s_x, int s_y, int s_w, int s_h, int d_x, int d_y, int d_w, int d_h)
	void stretch_sprite (BITMAP *bmp, BITMAP *sprite, int x, int y, int w, int h)

	int getpixel (BITMAP *bmp, int x, int y)
	void putpixel (BITMAP *bmp, int x, int y, int color)
	void vline (BITMAP *bmp, int x, int y_1, int y2, int color)
	void hline (BITMAP *bmp, int x1, int y, int x2, int color)
	void line (BITMAP *bmp, int x1, int y_1, int x2, int y2, int color)
	void fastline (BITMAP *bmp, int x1, int y_1, int x2, int y2, int color)
	void rectfill (BITMAP *bmp, int x1, int y_1, int x2, int y2, int color)
	void triangle (BITMAP *bmp, int x1, int y_1, int x2, int y2, int x3, int y3, int color)
	void polygon (BITMAP *bmp, int vertices, int *points, int color)
	void rect (BITMAP *bmp, int x1, int y_1, int x2, int y2, int color)
	void circle (BITMAP *bmp, int x, int y, int radius, int color)
	void circlefill (BITMAP *bmp, int x, int y, int radius, int color)
	void ellipse (BITMAP *bmp, int x, int y, int rx, int ry, int color)
	void ellipsefill (BITMAP *bmp, int x, int y, int rx, int ry, int color)
	
	# arc: ang1 & ang2 = fixeds
	void arc (BITMAP *bmp, int x, int y, int ang1, int ang2, int r, int color)
	void spline (BITMAP *bmp, int points[8], int color)
	void floodfill (BITMAP *bmp, int x, int y, int color)
	#void polygon3d (BITMAP *bmp, int type, BITMAP *texture, int vc, V3D *vtx[])
	#void polygon3d_f (BITMAP *bmp, int type, BITMAP *texture, int vc, V3D_f *vtx[])
	#void triangle3d (BITMAP *bmp, int type, BITMAP *texture, V3D *v1, V3D *v2, V3D *v3)
	#void triangle3d_f (BITMAP *bmp, int type, BITMAP *texture, V3D_f *v1, V3D_f *v2, V3D_f *v3)
	#void quad3d (BITMAP *bmp, int type, BITMAP *texture, V3D *v1, V3D *v2, V3D *v3, V3D *v4)
	#void quad3d_f (BITMAP *bmp, int type, BITMAP *texture, V3D_f *v1, V3D_f *v2, V3D_f *v3, V3D_f *v4)
	void draw_sprite (BITMAP *bmp, BITMAP *sprite, int x, int y)
	void draw_sprite_v_flip (BITMAP *bmp, BITMAP *sprite, int x, int y)
	void draw_sprite_h_flip (BITMAP *bmp, BITMAP *sprite, int x, int y)
	void draw_sprite_vh_flip (BITMAP *bmp, BITMAP *sprite, int x, int y)
	void draw_trans_sprite (BITMAP *bmp, BITMAP *sprite, int x, int y)
	void draw_lit_sprite (BITMAP *bmp, BITMAP *sprite, int x, int y, int color)
	void draw_gouraud_sprite (BITMAP *bmp, BITMAP *sprite, int x, int y, int c1, int c2, int c3, int c4)
	void draw_character_ex (BITMAP *bmp, BITMAP *sprite, int x, int y, int color, int bg)
	void rotate_sprite (BITMAP *bmp, BITMAP *sprite, int x, int y, fixed angle)
	void rotate_sprite_v_flip (BITMAP *bmp, BITMAP *sprite, int x, int y, fixed angle)
	void rotate_scaled_sprite (BITMAP *bmp, BITMAP *sprite, int x, int y, fixed angle, fixed scale)
	void rotate_scaled_sprite_v_flip (BITMAP *bmp, BITMAP *sprite, int x, int y, fixed angle, fixed scale)
	void pivot_sprite (BITMAP *bmp, BITMAP *sprite, int x, int y, int cx, int cy, fixed angle)
	void pivot_sprite_v_flip (BITMAP *bmp, BITMAP *sprite, int x, int y, int cx, int cy, fixed angle)
	void pivot_scaled_sprite (BITMAP *bmp, BITMAP *sprite, int x, int y, int cx, int cy, fixed angle, fixed scale)
	void pivot_scaled_sprite_v_flip (BITMAP *bmp, BITMAP *sprite, int x, int y, int cx, int cy, fixed angle, fixed scale)
	
	#############################################
	
	FONT *font
	int text_mode (int mode)
	void textout_ex (BITMAP *bmp, FONT *f, char *str, int x, int y, int color, int bg)
	void textout_centre_ex (BITMAP *bmp, FONT *f, char *str, int x, int y, int color, int bg)
	void textout_right_ex (BITMAP *bmp, FONT *f, char *str, int x, int y, int color, int bg)
	void textout_justify_ex (BITMAP *bmp, FONT *f, char *str, int x1, int x2, int y, int diff, int color, int bg)
	void textprintf_ex (BITMAP *bmp, FONT *f, int x, int y, int color, int bg, char *format, ...)
	void textprintf_centre_ex (BITMAP *bmp, FONT *f, int x, int y, int color, int bg, char *format, ...)
	void textprintf_right_ex (BITMAP *bmp, FONT *f, int x, int y, int color, int bg, char *format, ...)
	void textprintf_justify_ex (BITMAP *bmp, FONT *f, int x1, int x2, int y, int diff, int color, int bg, char *format, ...)
	int text_length (FONT *f, char *str)
	int text_height (FONT *f)
	void destroy_font (FONT *f)
	FONT * load_font (char *filename, RGB *pal, void *param)
	void textout (BITMAP *bmp, FONT *f, char *str, int x, int y, int color)
	void textout_centre (BITMAP *bmp, FONT *f, char *str, int x, int y, int color)
	void textout_right (BITMAP *bmp, FONT *f, char *str, int x, int y, int color)
	void textout_justify (BITMAP *bmp, FONT *f, char *str, int x1, int x2, int y, int diff, int color)
	void textprintf (BITMAP *bmp, FONT *f, int x, int y, int color, char *format, ...)
	void textprintf_centre (BITMAP *bmp, FONT *f, int x, int y, int color, char *format, ...)
	void textprintf_right (BITMAP *bmp, FONT *f, int x, int y, int color, char *format, ...)
	void textprintf_justify (BITMAP *bmp, FONT *f, int x1, int x2, int y, int diff, int color, char *format, ...)
	void draw_character (BITMAP *bmp, BITMAP *sprite, int x, int y, int color)
 	
	
	#############################################
	## Currently not implemented: fli, gui, packfile
	#############################################
	int alert (char *s1, char *s2, char *s3, char *b1, char *b2, int c1, int c2)
	int alert3 (char *s1, char *s2, char *s3, char *b1, char *b2, char *b3, int c1, int c2, int c3)
	int file_select_ex (char *message, char *path, char *ext, int size, int w, int h)
	int gfx_mode_select (int *card, int *w, int *h)
	int gfx_mode_select_ex (int *card, int *w, int *h, int *color_depth)
	
	#############################################
	
	
		
	SAMPLE *load_sample (char *filename)
	int save_sample (char *filename, SAMPLE *spl)
	SAMPLE * create_sample (int bits, int stereo, int freq, int len)
	void destroy_sample (SAMPLE *spl)
	int play_sample (SAMPLE *spl, int vol, int pan, int freq, int loop)
	void stop_sample (SAMPLE *spl)
	void adjust_sample (SAMPLE *spl, int vol, int pan, int freq, int loop)
	
	int install_sound (int digi, int midi, char *cfg_path)
	void remove_sound()
	void set_volume (int digi_volume, int midi_volume)
	void set_hardware_volume (int digi_volume, int midi_volume)
	void set_mixer_quality(int quality)
	int get_mixer_quality()
	int get_mixer_frequency()
	int get_mixer_bits()
	int get_mixer_channels()
	int get_mixer_voices()

	# Voices, streams, MIDI and aud input not (yet) implemented.
	# Most of the time you don't really need them.
	# File functions omitted, Python's got better ones.
	# Ditto for fixeds et al.

version="-- unknown --"
wrapperVersion="0.1.1"



# Generic error in the wrapper.
class PyallegError(Exception):
	pass
	
# Error in the Allegro core.
class AllegroError(PyallegError):
	def __init__(self):
		PyallegError.__init__(self,allegro_error)

# Error before or after the core.
class WrapperError(PyallegError):
	pass
	
def debug(s): pass #print "(pyalleg debug): "+s

sc=None
cdef public int nMouseB



###############################################################################
###############################################################################
# Class definitions ###########################################################
###############################################################################
###############################################################################

##############################################################################
                              ## Bitmaps ##
                              #############

cdef class AbstractBitmap:
	""" Base class for all bitmaps. Contains operations you do on bitmaps.
	You do not have to worry about cleaning memory, unless you really want to, or don't trust the Python garbage collection system. If you DO destroy() a Bitmap object, though, you WILL crash your application if you try to do anything with it.
	
	"""
	cdef BITMAP *bmp
	
	def destroy(self):
		if self.bmp!=NULL:
			debug("Destroying "+str(self))
			destroy_bitmap(self.bmp)
			self.bmp=NULL
	
	def clear(self):
		clear_bitmap(self.bmp)

	def clearTo(self,color):
		clear_to_color(self.bmp,color)
		
	def size(self):
		return self.bmp.w,self.bmp.h

	def putPixel(self,x,y,c):
		putpixel(self.bmp,x,y,c)

	def getPixel(self,x,y):
		return getpixel(self.bmp,x,y)
		
	def hline(self,x1,y,x2,c):
		hline(self.bmp,x1,y,x2,c)
		
	def vline(self,x,y1,y2,c):
		vline(self.bmp,x,y1,y2,c)
		
	def line(self,x1,y1,x2,y2,c):
		line(self.bmp,x1,y1,x2,y2,c)
		
	def fastline(self,x1,y1,x2,y2,c):
		fastline(self.bmp,x1,y1,x2,y2,c)
	
	def rect(self,x1,y1,x2,y2,c):
		rect(self.bmp,x1,y1,x2,y2,c)
	
	def fillRect(self,x1,y1,x2,y2,c):
		rectfill(self.bmp,x1,y1,x2,y2,c)
		
	def rectfill(self,x1,y1,x2,y2,c):
		rectfill(self.bmp,x1,y1,x2,y2,c)
		
	
	def triangle(self,x1,y1,x2,y2,x3,y3,c):
		triangle(self.bmp,x1,y1,x2,y2,x3,y3,c)
		
	def polygon(self,lpoints,c,filled=1):
		cdef int points[1000]
		l=len(lpoints)
		if l>500: l=500
		for i from 0<=i<l:
			points[i*2]=lpoints[i][0]
			points[i*2+1]=lpoints[i][1]
		polygon(self.bmp,l,points,c)
	
	def circle(self,x,y,r,c):
		circle(self.bmp,x,y,r,c)
	
	def fillCircle(self,x,y,r,c):
		circlefill(self.bmp,x,y,r,c)
		
	def circlefill(self,x,y,r,c):
		circlefill(self.bmp,x,y,r,c)

	def ellipse(self,x,y,rx,ry,c):
		ellipse(self.bmp,x,y,rx,ry,c)
	
	def fillEllipse(self,x,y,rx,ry,c):
		ellipsefill(self.bmp,x,y,rx,ry,c)

	def ellipsefill(self,x,y,rx,ry,c):
		ellipsefill(self.bmp,x,y,rx,ry,c)
	
	
	def blit(self,AbstractBitmap dest,dx=0,dy=0,sx=0,sy=0,w=-1,h=-1):	
		if w>-1:	rw,rh=w,h
		else:		rw,rh=self.size()
			
		blit(self.bmp, dest.bmp, sx, sy, dx, dy, rw,rh)

	def maskedBlit(self,AbstractBitmap dest,dx=0,dy=0,sx=0,sy=0,w=-1,h=-1):	
		if w>-1:	rw,rh=w,h
		else:		rw,rh=self.size()
			
		masked_blit(self.bmp, dest.bmp, sx, sy, dx, dy, rw,rh)

	def stretchBlit(self,AbstractBitmap dest,dx=0,dy=0,sx=0,sy=0,srcw=-1,srch=-1,dw=-1,dh=-1):	
		if srcw>-1:	sw,sh=srcw,srch
		else:		srcw,srch=self.size()
		
		if dw>-1:	destw,desth=dw,dh
		else:		destw,desth=srcw,srch
			
		stretch_blit (self.bmp, dest.bmp, sx, sy, sw, sh, destx, desty, dw, dh)

	def maskedStretchBlit(self,AbstractBitmap dest,dx=0,dy=0,sx=0,sy=0,srcw=-1,srch=-1,dw=-1,dh=-1):
		if srcw>-1:	sw,sh=srcw,srch
		else:		srcw,srch=self.size()
		
		if dw>-1:	destw,desth=dw,dh
		else:		destw,desth=srcw,srch
			
		masked_stretch_blit (self.bmp, dest.bmp, sx, sy, sw, sh, destx, desty, dw, dh)
	
	def drawSprite(self,AbstractBitmap dest,x,y,flips=0,w=-1,h=-1):
		if w>-1:
			stretch_sprite (dest.bmp, self.bmp, x, y, w, h)
		else:
			if flips==0:	# not flipped
				draw_sprite (dest.bmp, self.bmp, x, y)
			elif flips==1:	# v flipped 
				draw_sprite_v_flip (dest.bmp, self.bmp, x, y)
			elif flips==2:	# h flipped 
				draw_sprite_h_flip (dest.bmp, self.bmp, x, y)
			elif flips==3:	# vh flipped 
				draw_sprite_vh_flip (dest.bmp, self.bmp, x, y)
			else:
				raise WrapperError,"Illegal flipping mode, 0-3 are legal."
				
	def drawTransSprite(self,AbstractBitmap dest,x,y):
		draw_trans_sprite (dest.bmp, self.bmp, x, y)
		
	def drawLitSprite(self,AbstractBitmap dest,x,y, light):
		draw_lit_sprite (dest.bmp, self.bmp, x, y, light)
	
	def drawGouraudSprite(self,AbstractBitmap dest,x,y,l1,l2,l3,l4):
		draw_gouraud_sprite (dest.bmp, self.bmp, x, y,l1,l2,l3,l4)
	
	def rotateSprite(self,AbstractBitmap dest,x,y,angle,scale=1.0,vflip=0):
		cdef fixed fangle,fscale
		fangle=ftofix(angle)
		if scale==1.0:
			if vflip:
				rotate_sprite_v_flip(dest.bmp,self.bmp,x,y,fangle)
			else:
				rotate_sprite(dest.bmp,self.bmp,x,y,fangle)
		else:
			fscale=ftofix(scale)
			if vflip:
				rotate_scaled_sprite_v_flip(dest.bmp,self.bmp,x,y,fangle,fscale)
			else:
				rotate_scaled_sprite(dest.bmp,self.bmp,x,y,fangle,fscale)
	
	def pivotSprite(self,AbstractBitmap dest,x,y,px,py,angle,scale=1.0,vflip=0):
		cdef fixed fangle,fscale
		fangle=ftofix(angle)
		if scale==1.0:
			if vflip:
				pivot_sprite_v_flip(dest.bmp,self.bmp,x,y,px,py,fangle)
			else:
				pivot_sprite(dest.bmp,self.bmp,x,y,px,py,fangle)
		else:
			fscale=ftofix(scale)
			if vflip:
				pivot_scaled_sprite_v_flip(dest.bmp,self.bmp,x,y,px,py,fangle,fscale)
			else:
				pivot_scaled_sprite(dest.bmp,self.bmp,x,y,px,py,fangle,fscale)
					
	def save(self,filename):
		if save_bitmap(filename,self.bmp,NULL)!=0:
			raise AllegroError()
	

		
		
cdef class Bitmap(AbstractBitmap):
	def __new__(self,w,h,d=0):
		debug("Creating memory bitmap "+str((w,h,d)))
		if d>0:
			self.bmp=create_bitmap_ex(d,w,h)
		else:
			self.bmp=create_bitmap(w,h)
		if self.bmp==NULL:
			raise AllegroError()

	def __dealloc__(self):
		if self.bmp!=NULL:
			debug("deallocing bitmap: "+str(self)+"!")
			allegro_init()	# ugly-ish kludge.. *shrug*
			destroy_bitmap(self.bmp)
		else:
			debug("bitmap already deallocd: "+str(self)+"!")
		debug("finished")

		
cdef class FileBitmap(AbstractBitmap):
	def __new__(self,filename):
		debug("Loading bitmap "+filename)
		self.bmp=load_bitmap(filename,NULL)
		if self.bmp==NULL:
			raise AllegroError()
			
	def __dealloc__(self):
		if self.bmp!=NULL:
			destroy_bitmap(self.bmp)			
			
def loadBitmap(filename):
	return FileBitmap(filename)

cdef class ScreenBitmap(AbstractBitmap):
	def __new__(self):
		debug("Creating screen bitmap")
		self.bmp=screen
	
	def __dealloc__(self):
		pass
		
	def size(self):
		return SCREEN_W,SCREEN_H,VIRTUAL_W,VIRTUAL_H

##############################################################################
                               ## Font ##
                               ##########

cdef class Font:
	cdef FONT *f
	
	def __new__(self,filename=""):
		if filename!="":
			self.f=load_font(filename,NULL,NULL)
		else:
			self.f=font
	
	def __dealloc__(self):
		if self.f!=NULL and self.f!=font:
			allegro_init()
			destroy_font(self.f)

	def draw(self,AbstractBitmap dest,x,y,c,text,mode=0,bg=-1):
		if mode==0:	# Left.
			textout_ex(dest.bmp,self.f,text,x,y,c,bg)
		elif mode==1:	# Center.
			textout_centre_ex(dest.bmp,self.f,text,x,y,c,bg)
		elif mode==2:	# Right.
			textout_right_ex(dest.bmp,self.f,text,x,y,c,bg)
		else:
			raise WrapperError("Invalid font drawing mode (0-2).")

	def justify(self,AbstractBitmap dest,x1,x2,y,diff,text,bg=-1):
		textout_justify_ex(dest.bmp,self.f,text,x1,x2,y,diff,c,bg)

	def height(self):
		return text_height(self.f)

	def length(self,text):
		return text_length(self.f,text)

	def width(self,text):
		return text_length(self.f,text)

##############################################################################
                              ## Sound ##
                              ###########

	
cdef class Sample:
	cdef SAMPLE *sample

	def __new__(self,filename):
		self.sample=load_sample(filename)
		if self.sample==NULL:
			raise AllegroError
	
	def length(self):
		return self.sample.len/float(self.sample.freq)

	def play(self,loop=0,vol=255,pan=0,freq=1000):
		play_sample(self.sample,vol,pan+127,freq,loop)

	def stop(self):
		stop_sample(self.sample)

	def adjust(self,loop=0,vol=255,pan=0,freq=1000):
		adjust_sample(self.sample,vol,pan+127,freq,loop)

##############################################################################
                              ## Timers ##
                              ############

def getTime():
	return time.clock()
	
def delay(t):
	now=getTime()
	while (getTime()-now)<=t:
		pass

class FPSTimer:
	def __init__(self,fps=50.0):
		self.lastTick=getTime()
		self.n=0
		self.fps=float(fps)
		
	def tick(self):
		ifps=1.0/self.fps
		nt=getTime()
		d=ifps-(nt-self.lastTick)
		delay(d)
		self.lastTick=nt
		
###############################################################################
###############################################################################
# Func definitions ############################################################
###############################################################################
###############################################################################

def exit():
	allegro_exit()

def init():
	import atexit
	global version
	if allegro_init()!=0:
		raise AllegroError()
	version=allegro_id+" (PyAlleg "+wrapperVersion+")"
	debug("Initialized: "+version)
	atexit.register(exit)
	return version

def setWindowTitle(text):
	set_window_title(text)

	
def initKeyboard():
	debug("Initializing keyboard...")
	if install_keyboard()!=0:
		raise AllegroError()
		
def initMouse():
	
	debug("Initializing mouse...")
	mb=install_mouse()
	if mb<0:
		raise AllegroError()
	if mb>0: nMouseB=mb
		
def initGfx(m,w,h,d=-1,vw=0,vh=0):
	global sc
	debug("Beginning graphics initialization...")
	if d==-1:
		d=desktop_color_depth()
	set_color_depth(d)
	if m==0:	# Windowed
		if set_gfx_mode (2,w,h,vw,vh)<0:
			raise AllegroError()
	elif m==1:
		if set_gfx_mode (1,w,h,vw,vh)<0:
			raise AllegroError()
	else:
		raise WrapperError("Unknown graphics mode. Valid values are 0 and 1.")
	debug("Finished graphics init.")
	if sc==None:
		debug("Creating screen wrapper object.")
		sc=ScreenBitmap()
	else:
		debug("Screen wrapper already available.")

def initSound():
	if install_sound (-1,0,NULL)==-1:
		raise AllegroError()
	
def getScreen():
	return sc
	
def getFont():
	return Font()
	
def keyDown(int k):
	if k<0 or k>256:
		return 0
	return key[k]
	
def keyPressed():
	return keypressed()
	
def keyMods():
	return key_shifts

def mouseX():
	return mouse_x
	
def mouseY():
	return mouse_y

def mouseZ():
	return mouse_z

def mouseB():
	return mouse_b

def mouse():
	return mouse_x,mouse_y,mouse_z,mouse_b
	
def mickeys():
	cdef int mix,miy
	get_mouse_mickeys(&mix,&miy)
	return mix,miy
	
def drawMode(mode, AbstractBitmap pattern=None, x=0,y=0):
	if mode>=0 and mode<6:
		if pattern!=None:
			drawing_mode(mode,pattern.bmp,x,y)
		else:
			drawing_mode(mode,NULL,0,0)
	else:
		raise WrapperError("Invalid drawing mode, valid values are 0-5.")

def solidMode():
	drawMode(0)
	
def xorMode():
	drawMode(1)
	
def transMode():
	drawMode(5)

def rgbHsv(r,g,b):
	cdef float h,s,v
	rgb_to_hsv(r,g,b,&h,&s,&v)
	return (h,s,v)

def hsvRgb(h,s,v):
	cdef int r,g,b
	hsv_to_rgb(h,s,v,&r,&g,&b)
	return (r,g,b)

def setBlender(blender,a=255,r=255,g=255,b=255):
	if blender=="alpha":		set_alpha_blender()
	elif blender=="walpha":		set_write_alpha_blender()
	elif blender=="trans":		set_trans_blender(r,g,b,a)
	elif blender=="add":		set_add_blender(r,g,b,a)
	elif blender=="burn":		set_burn_blender(r,g,b,a)
	elif blender=="color":		set_color_blender(r,g,b,a)
	elif blender=="diff":		set_difference_blender(r,g,b,a)
	elif blender=="dissolve":	set_dissolve_blender(r,g,b,a)
	elif blender=="dodge":		set_dodge_blender(r,g,b,a)
	elif blender=="hue":		set_hue_blender(r,g,b,a)
	elif blender=="invert":		set_invert_blender(r,g,b,a)
	elif blender=="lumi":		set_luminance_blender(r,g,b,a)
	elif blender=="mult":		set_multiply_blender(r,g,b,a)
	elif blender=="sat":		set_saturation_blender(r,g,b,a)
	elif blender=="screen":		set_screen_blender(r,g,b,a)
	else:
		raise WrapperError("Invalid blender, check the blenders table in constants.")

def setTrans(a):
	setBlender("trans",a)
	transMode()

def setAdd(a):
	setBlender("add",a)
	transMode()
	


	
################################################################################
## pseudo-classes ##############################################################
################################################################################

def Color(r,g,b,a=-1):
	if a==-1: return makecol(r,g,b)
	return makeacol(r,g,b,a)