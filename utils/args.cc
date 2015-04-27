#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>  
#include <assert.h>

#define BUF_LEN 1024

enum {
	FILE_PARAM = 1,
	PIPE_PARAM = 2,
	STD_PARAM = 3
};

int parse_param(char *param, char *acc) {
	int len = strlen(param);
	if('-' == param[0]) return STD_PARAM;
	if('|' == param[len - 1]) {
		strncpy(acc, param, len - 1);
		acc[len-1] = '\0';	
		return PIPE_PARAM;
	}
	strcpy(acc, param);
	return FILE_PARAM;	
}

void test() {
	char buf[BUF_LEN] = {0};
	int type = parse_param("test.txt", buf);
	assert(type == FILE_PARAM);
	assert(strcmp(buf, "test.txt") == 0);
	type = parse_param("cat test.txt|", buf);
	assert(type == PIPE_PARAM);
	assert(strcmp(buf, "cat test.txt") == 0);
	type = parse_param("-", buf);
	assert(type == STD_PARAM);
}

void little_cat(int type, char *cmd) {
	FILE *fp;
	switch(type) {
		case FILE_PARAM:
			fp = fopen(cmd, "r");
			if(!fp) {
				printf("file %s not exist\n", cmd);
			}
			while(!feof(fp)) {
				putchar(getc(fp));
			}	
			fclose(fp);
			break;
		case STD_PARAM:
			while(true) {
				putchar(getchar());
			}
			break;
		case PIPE_PARAM:
			fp = popen(cmd, "r");
			while(!feof(fp)) {
				putchar(getc(fp));
			}	
			pclose(fp);
			break;
		default:
			assert(false);
	}	
}

int main(int argc, char *argv[]) {
	char param_buf[BUF_LEN] = {0}; 
	int cur = 0;
	int type;
	char param[BUF_LEN] = {0};
	for(int i = 1; i < argc; i++) {
		strcpy(param_buf+cur, argv[i]);
		cur	+= strlen(argv[i]);
		param_buf[cur] = ' ';
		cur +=1;
	}
	param_buf[cur-1] = '\0';
	//test();
	printf("%s\n", param_buf);
	type = parse_param(param_buf, param);
	printf("%d %s\n", type, param);
	little_cat(type, param);
	return 0;
}
