#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

int main(void) {
    fd_set rfds;
    struct timeval tv;
    int retval;
    char buf[1024];
    while (1) {
        /* Watch stdin (fd 0) to see when it has input. */
        FD_ZERO(&rfds);
        FD_SET(0, &rfds);

        /* Wait up to five seconds. */
        tv.tv_sec = 5;
        tv.tv_usec = 0;

        switch(select(0+1, &rfds, NULL, NULL, &tv)) {
            case -1: perror("select()"); exit(-1);
            case 0:  printf("time out\n"); continue;
            default: {
                if (FD_ISSET(0, &rfds)) {
                    scanf("%s", buf); 
                    printf("%s\n", buf);
                }
            }
        }
    }
    /* FD_ISSET(0, &rfds) will be true. */
    return 0;
}
