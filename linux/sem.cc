#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

#include <vector>
int sum = 0;
sem_t sem;

void *thread_func(void *args) {
    for (int i = 0; i < 10000; i++) {
        sem_wait(&sem);
        sum++;
        sem_post(&sem);
    }
}

int main() {
    std::vector<pthread_t> tid(5, 0);
    sem_init(&sem, 0, 1);
    for (int i = 0; i < tid.size(); i++) {
       int r = pthread_create(&tid[i], NULL, thread_func, NULL); 
    }

    for (int i = 0; i < tid.size(); i++) {
       pthread_join(tid[i], NULL);  
    }
    printf("%d\n", sum);
}
