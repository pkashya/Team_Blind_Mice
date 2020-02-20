#include <stdio.h>
#include <liblouis/liblouis.h>

int main(){
  FILE *fp;
   int c;
   int n = 0;
   int ind = 0;
  
   fp = fopen("tmp1.txt","r");
   if(fp == NULL) {
      perror("Error in opening file");
      return(-1);
   } do {
    ind++;
      c = fgetc(fp);
      if( feof(fp) ) {
         break ;
      }
      if(!(ind%3)){
        int count = 0;
        //printf("%x\n",c );
        while (c) {
          count++;
        if (c & 1)
           printf("1");
        else
            printf("0");
        if (count == 6)
          break;

      c >>= 1;
  }
  printf("\n");
      }

   } while(1);

   fclose(fp);
  return 0;
}
