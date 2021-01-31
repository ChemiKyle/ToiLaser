#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define LED_PIN 4 // D2
#define PIR_PIN 5 // D1
#define MQTT_TOPIC "toilaser"

// WiFi and MQTT setup
const char* ssid = ""; // your wifi name
const char* password = ""; // your wifi password
const char* mqtt_server = ""; // the ip address of your rpi
const char* toilaser_location = "0"; // this needs to be a single char increment for every bathroom

int pirState = LOW;
int val = 0;

WiFiClient espClient;
PubSubClient client(espClient);

void callback(char* topic, byte* payload, unsigned int length) {
    // used to act on messages from the MQTT server
    // we're not actually going to end up using this
    for (int i=0;i<length;i++) {
        char receivedChar = (char)payload[i];
        Serial.print(receivedChar);
        if (receivedChar == '0'){
            // turn off
        }
        else if (receivedChar == '1') {
            // turn back on
        }
    }
    Serial.println();
}

void reconnect() {
    // attempt to connect to MQTT
    while (!client.connected()) {
        Serial.print("Attempting MQTT connection...");
        // assign random client ID to avoid collisions
        // adapted from: https://github.com/knolleary/pubsubclient/blob/master/examples/mqtt_esp8266/mqtt_esp8266.ino
        String clientID = "toilaser-";
        clientID += String(toilaser_location);
        clientID += String(random(0xffff), HEX);

        if (client.connect(clientID.c_str())) {
            Serial.println("connected");
            client.subscribe(MQTT_TOPIC);
        } else {
            // keep trying to connect
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" try again in 5 seconds");
            delay(5000);
        }
    }
}

void setup() {
    // connect to WiFi
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) { delay(500); }
    Serial.println("Connected to wifi");
    Serial.println(WiFi.localIP());

    // connect to MQTT
    client.setServer(mqtt_server, 1883);
    client.setCallback(callback);

    pinMode(LED_PIN, OUTPUT);
    pinMode(PIR_PIN, INPUT);

    Serial.begin(9600);

    // cycle laser so we know it's working
    digitalWrite(LED_PIN, HIGH);
    delay(500);
    digitalWrite(LED_PIN, LOW);
}

void loop() {
    // reconnect to MQTT if disconnect occured
    if (!client.connected()) {
        reconnect();
    }
    client.loop();

    // laser loop
    // adapted from: https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/using-a-pir-w-arduino
    val = digitalRead(PIR_PIN);
    if (val == HIGH) {
        digitalWrite(LED_PIN, HIGH);
        if (pirState == LOW) {
            Serial.println("Motion detected!");
            pirState = HIGH;
            client.publish(MQTT_TOPIC, toilaser_location);

            delay(5*1000*60); // "debounce" with 5 minute wait
        }
    } else {
        digitalWrite(LED_PIN, LOW);
        if (pirState == HIGH){
            Serial.println("Motion ended!");
            pirState = LOW;
        }
    }
}
