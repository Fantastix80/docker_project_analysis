# python-kafka-docker
Voici le projet github de base

Nous avons effectué quelques modifications pour que celui-ci soit fonctionnel.

Pour le faire fonctionner, télécharger le projet présent sur ce github, puis rajouter un fichier .env dans consumer et un fichier .env dans producer avec la configuration suivante:
KAFKA_TOPIC_NAME=topic_test
KAFKA_SERVER=kafka
KAFKA_PORT=29092

Ensuite, lancez simplement le docker à l'aide de la commande suivante: docker-compose up --build -d

Pour tester le projet, rendez-vous sur l'url suivante: http://localhost:19000/ puis sélectionnez le topic topic_test, Appuyez ensuite sur "Voir les messages". Cela vous emmenera sur une page où vous pourrez visualiser les messages envoyés sur ce topic.

Pour envoyer les messages, rendez-vous sur l'url suivante: http://localhost:8000/docs puis cliquez sur "Producer". Cela ouvrira un menu déroulant dans lequel vous appuyerez sur le bouton "try it out" puis il vous suffira de modifier le json à votre guise et d'appuyer sur "execute". Ensuite retournez sur l'autre page et rafraichissez la afin de visualiser le message envoyé.
