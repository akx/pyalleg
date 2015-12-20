/* PyAlleg bonus functions.
   I know it's bad to put code in #includes, but I'm lazy.
*/


#ifdef __linux__
  // This is a hack to make PNG support *compile* under Linux.
  // Sigh.
  #define PNG_NO_SETJMP_SUPPORTED
#endif
#include "loaders/loadpng.c"
#include "loaders/savepng.c"

#include "loaders/jpgalleg.c"
#include "loaders/algif/algif.c"
#include "loaders/algif/gif.c"
#include "loaders/algif/lzw.c"
#include "loaders/ttf.c"

BITMAP **animFrames;
int *animDura;
int animCount;

void initLoaders()
{
	register_bitmap_file_type("png", load_png, save_png);
	register_bitmap_file_type("jpg", load_jpg, NULL);
	register_bitmap_file_type("jpeg", load_jpg, NULL);
	register_bitmap_file_type("jfif", load_jpg, NULL);
	register_bitmap_file_type("gif", load_gif, save_gif);
	alfont_init();
}

void exitLoaders()
{
	alfont_exit();
}

void _loadAnim(char *file)
{
	animCount=algif_load_animation(file, &animFrames, &animDura);
}

void _freeAnim()
{
	free(animDura);
	free(animFrames);
}
