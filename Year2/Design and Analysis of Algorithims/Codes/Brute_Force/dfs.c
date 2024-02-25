#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

int visited[MAX_VERTICES];
int color[MAX_VERTICES];

typedef struct
{
    int vertices[MAX_VERTICES];
    int front, rear;
} Queue;

void initializeQueue(Queue *q)
{
    q->front = -1;
    q->rear = -1;
}

int isEmpty(Queue *q)
{
    return q->front == -1;
}

void enqueue(Queue *q, int vertex)
{
    if (isEmpty(q))
    {
        q->front = 0;
    }
    q->rear++;
    q->vertices[q->rear] = vertex;
}

int dequeue(Queue *q)
{
    int vertex = q->vertices[q->front];
    if (q->front == q->rear)
    {
        q->front = -1;
        q->rear = -1;
    }
    else
    {
        q->front++;
    }
    return vertex;
}

int isBipartiteDFS(int graph[MAX_VERTICES][MAX_VERTICES], int vertices, int currentVertex, int c)
{
    visited[currentVertex] = 1;
    color[currentVertex] = c;

    for (int i = 0; i < vertices; i++)
    {
        if (graph[currentVertex][i] == 1)
        {
            if (!visited[i])
            {
                if (!isBipartiteDFS(graph, vertices, i, 1 - c))
                {
                    return 0;
                }
            }
            else if (color[i] == color[currentVertex])
            {
                return 0;
            }
        }
    }
    return 1;
}

int isBipartite(int graph[MAX_VERTICES][MAX_VERTICES], int vertices)
{
    for (int i = 0; i < vertices; i++)
    {
        visited[i] = 0;
        color[i] = -1;
    }

    for (int i = 0; i < vertices; i++)
    {
        if (!visited[i])
        {
            if (!isBipartiteDFS(graph, vertices, i, 0))
            {
                return 0;
            }
        }
    }
    return 1;
}

int main()
{
    int vertices, edges;

    printf("Enter the number of vertices and edges: ");
    scanf("%d %d", &vertices, &edges);

    int graph[MAX_VERTICES][MAX_VERTICES] = {0};

    printf("Enter the edges (vertex1 vertex2):\n");
    for (int i = 0; i < edges; i++)
    {
        int vertex1, vertex2;
        scanf("%d %d", &vertex1, &vertex2);
        graph[vertex1][vertex2] = 1;
        graph[vertex2][vertex1] = 1;
    }

    if (isBipartite(graph, vertices))
    {
        printf("The graph is bipartite.\n");
    }
    else
    {
        printf("The graph is not bipartite.\n");
    }

    return 0;
}
