#include <stdio.h>
#include <liblouis/liblouis.h>

int main(){

  FILE *fp;
   char str[60];
   char tmp[60];

   /* opening file for reading */
   fp = fopen("test1.txt" , "r");
   if(fp == NULL) {
      perror("Error opening file");
      return(-1);
   }
   if( fgets (str, 60, fp)!=NULL ) {
      /* writing content to stdout */
      puts(str);
   }
   fclose(fp);

  lou_translateString(en-us-g2,str,60,tmp,60);







  return 0;
}
