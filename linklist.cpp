#include<bits/stdc++.h>
using namespace std;

class Node{ 
    public:
    int data;
    Node*next;
    Node(int data){ 
    this->data=data;
    this->next=next;
    }
};

void insertathead(Node*&head,int data){
    Node*temp=new Node(data);
    temp->next =head;
    head=temp;
}
void insertatend(Node*&tail,int data){ 
    Node*temp=new Node(data);
    tail->next=temp;
    tail=temp;

}
void insertany(Node*&tail,Node*&head,int position,int data){  
    Node*nodetoinsert=new Node(data);
    Node*temp=head;
    int cnt=1;
    if(position==1){ 
        insertathead(head,data);
        return;
    }
    while (cnt<position-1)
    {
        temp=temp->next;
        cnt++;
    }
    if(temp->next==NULL){ 
        insertatend(tail,data);
        return;
    }
    
    nodetoinsert->next=temp->next;
    temp->next=nodetoinsert;
}

void printin(Node*node){ 
    while(node!=NULL){
        cout<<node->data<<" ";
        node=node->next;
    }
    cout<<endl;

}

int main(){ 
    Node*node1=new Node(10);
    Node*head=node1;
    Node*tail=node1;
    insertathead(head,2);
    insertatend(tail,9);
    insertany(tail,head,2,68);
    printin(head);


}