#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

int color[MAX_VERTICES];

typedef struct {
    int vertices[MAX_VERTICES];
    int front, rear;
} Queue;

void initializeQueue(Queue *q) {
    q->front = -1;
    q->rear = -1;
}

int isEmpty(Queue *q) {
    return q->front == -1;
}

void enqueue(Queue *q, int vertex) {
    if (isEmpty(q)) {
        q->front = 0;
    }
    q->rear++;
    q->vertices[q->rear] = vertex;
}

int dequeue(Queue *q) {
    int vertex = q->vertices[q->front];
    if (q->front == q->rear) {
        q->front = -1;
        q->rear = -1;
    } else {
        q->front++;
    }
    return vertex;
}

int isBipartiteBFS(int graph[MAX_VERTICES][MAX_VERTICES], int vertices, int startVertex) {
    Queue q;
    initializeQueue(&q);

    for (int i = 0; i < vertices; i++) {
        color[i] = -1;
    }

    color[startVertex] = 0;
    enqueue(&q, startVertex);

    while (!isEmpty(&q)) {
        int currentVertex = dequeue(&q);

        for (int i = 0; i < vertices; i++) {
            if (graph[currentVertex][i] == 1) {
                if (color[i] == -1) {
                    color[i] = 1 - color[currentVertex];
                    enqueue(&q, i);
                } else if (color[i] == color[currentVertex]) {
                    return 0;
                }
            }
        }
    }

    return 1;
}

int main() {
    int vertices, edges;

    printf("Enter the number of vertices and edges: ");
    scanf("%d %d", &vertices, &edges);

    int graph[MAX_VERTICES][MAX_VERTICES] = {0};

    printf("Enter the edges (vertex1 vertex2):\n");
    for (int i = 0; i < edges; i++) {
        int vertex1, vertex2;
        scanf("%d %d", &vertex1, &vertex2);
        graph[vertex1][vertex2] = 1;
        graph[vertex2][vertex1] = 1;
    }

    if (isBipartiteBFS(graph, vertices, 0)) {
        printf("The graph is bipartite.\n");
    } else {
        printf("The graph is not bipartite.\n");
    }

    return 0;
}
