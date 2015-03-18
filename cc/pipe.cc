#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <assert.h>

#define BUF_SIZE 1024

int main() {
    system("read -p \"press any key to continue\"");

    char buf[BUF_SIZE];
    FILE *fp = popen("ls", "r");
    assert(fp != NULL);
    while(!feof(fp)) {
        fgets(buf, BUF_SIZE, fp);
        printf("%s", buf);
    }
    pclose(fp);
    return 0;
}
