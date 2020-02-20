#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
 
#define MAXCHAR 1000

int main()
{
    FILE * fp;
   wchar_t mystring [100];

   fp = fopen ("tmp1.txt" , "r");
   if (fp != NULL)
   {
     if ( fgetws (mystring , 100 , fp) != NULL )
       fputws ( mystring, stdout );
   }
   printf("a = %c", mystring[1]);



    /*do {
      c = fgetc(fp);
      if( feof(fp) ) {
         break ;
      }

      switch (c)
      {
      	case '⠠':
      	printf("000001");
      	break;

    	case '⠁':
      	printf("100000");
      	break;

      	case '⠝':
      	printf("101110");
      	break;

    default:
      printf("000000");
}

   } while(1);*/

    fclose(fp);
    return 0;
}