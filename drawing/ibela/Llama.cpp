#ifndef _LLAMA_CPP_
#define _LLAMA_CPP_

#include "Llama.h"
#include <string>
#include <iostream>
template <class T, int LN_SIZE>
Llama<T,LN_SIZE>::Llama() {
    LlamaNode<T, LN_SIZE> *tmp;
    head = tmp;
    tail = tmp;
}

template <class T, int LN_SIZE>
Llama<T,LN_SIZE>::~Llama() {
    while (nodeAmount > 0) {
        LlamaNode<T, LN_SIZE> *currentPtr = head;
        LlamaNode<T, LN_SIZE> *tempPtr;

        while ( currentPtr != NULL ) // delete remaining nodes
        {  
            tempPtr = currentPtr;
            currentPtr = currentPtr->m_next;
            delete tempPtr;
            nodeAmount--;
        }
    }
    Llama();
}

template <class T, int LN_SIZE>
void Llama<T,LN_SIZE>::push(const T& data) {
    if (s == LN_SIZE * nodeAmount) {
        LlamaNode<T, LN_SIZE> *tmp;
        tail->m_next = tmp;
        tail = tail->m_next;
    }
    
    tail->arr[s % LN_SIZE] = data;
    s++;
}

template <class T, int LN_SIZE>
T Llama<T,LN_SIZE>::pop() {
    if (s % LN_SIZE >= LN_SIZE / 2) {
        LlamaNode<T, LN_SIZE> *tmp;
        tmp = tail->m_next;
        nodeAmount--;
        delete tmp;
    }
    T& data = tail->arr[s % LN_SIZE];
    std::cout << tail->arr << std::endl;
    s--;

    return data;
}

int main () {
    Llama<int, 2> a;
    a.push(1);
    a.push(2);
    a.push(1);
    a.push(2);
    a.pop() ;
    std::cout << a.pop() << std::endl;
}
#include "Llama.cpp"
#endif