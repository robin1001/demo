#include <stdio.h>
#include <pthread.h>

#include <vector>

int sum = 0;
pthread_mutex_t mutex;

void *thread_func(void *args) {
    for (int i = 0; i < 10000; i++) {
        pthread_mutex_lock(&mutex);
        sum++;
        pthread_mutex_unlock(&mutex);
    }
}

int main() {
    std::vector<pthread_t> tid(5, 0);
    for (int i = 0; i < tid.size(); i++) {
       int r = pthread_create(&tid[i], NULL, thread_func, NULL); 
    }

    for (int i = 0; i < tid.size(); i++) {
       pthread_join(tid[i], NULL);  
    }
    printf("%d\n", sum);
}
