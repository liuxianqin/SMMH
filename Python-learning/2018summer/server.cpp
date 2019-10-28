#include<Winsock_32.h>
#include<stdio.h>
#include<stdlib.h>

#define DEFAULT_PORT 5050
#define BUFFER_LENGTH 1024

void main(){
	int iPort=DEFAULT_PORT;
	WSADATA wsaData;
	SOCKET sSocket;
	int iLen;
	int iSend;
	int iRecv;
	char send_buf[]="Hello,i am a server!";
	char recv_buf[BUFFER_LENGTH];
	struct sockaddr_in ser,
			   cli;
	printf("*****************\n");
	printf("Server waiting...\n");
	printf("*****************\n");
	if(WSAStartup(MAKEWORD(2,2),&wsaData)!=0){
		printf("Failed to load Winsock.\n");
		return;
	}
	sSocket=socket(AF_INET,SOCK_DGRAM,0);
	if(sSocket==INVALD_SOCKET){
		printf("socket() Failed:%d\n",WSAGetLastError());
		return;
	}
	ser.sinfamily=AF_INET;
	ser.sin_port=htons(iPort);
	ser.sin_addr.s_addr=htonl(INADDR_ANY);
	if(bind(sSocket,(LPSOCKADDR)&ser,sizeof(ser))==SOCKET_ERROR){
		printf("bind() Failed:%d",WSAGetLastError());
		return;
	}
	iLen=sizeof(cli);
	memset(recv_buf,0,sizeof(recv_buf));
	while(1){
		iRecv=recvfrom(sSocket,recv_buf,BUFFER_LENGTH,0,(SOCKADDR*)&cli,&iLen);
		if(iRecv==SOCKET_ERROR){
			printf("recvfrom() Failed:%d\n",WSAGetLastError());
			break;
		}
		else if(iRecv==0)
			break;
			else
			{
				printf("recvfrom():%s\n",recv_buf);
				printf("Accepted client IP:[%s],port[%d]\n",
						inet_ntoa(cli.sin_addr),
						ntohs(cli.sin_port));
			}
		iSend=sendto(sSocket,send_buf,sizeof(send_buf),0,(SOCKADDR*)&cli,sizeof(cli));
		if(iSend==SOCKET_ERROR){
			printf("sendto() Failed:%s\n",WSAGetLastError());
			printf("******************8\n");
			break;
		}
		else if(iSend==0){
			break;
			else {
				printf("sendto() succeed!\n");
				printf("******************\n");
			}
		}
		closesocket(sSocket);
		WSACleanup();
	}
