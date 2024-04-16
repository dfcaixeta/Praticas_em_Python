''' Criando um diagrama de rede usando as bibliotecas diagrams. 

Observações importantes:

    1. É necessário instalar o Microsoft Visual C++ 14.0 (ou versão superior)
    Obtenha em "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

    2. Tem que baixar e instalar o programa Graphviz instalar e adicionar o path nas variáveis do sistema.
    Obtenha em: https://graphviz.org/download/.
    - Para adicionar o path copie o caminho do programa até a pasta /bin -> C:\Program Files\Graphviz\bin
    - Execute o atalho Win + I -> Sistema -> Sobre -> Configurações avançadas do sistema -> Variáveis de Ambiente ...
      Variáveis do sistema -> Path e Editar -> Adicione o path acima.

    3. Explicações das Conexões no Diagrama:
    - DNS para Load Balancer: As requisições começam no serviço DNS e são direcionadas para o balanceador
      de carga.
    - Load Balancer para Serviços ECS: O balanceador de carga distribui o tráfego entre os servidores ECS.
    - Serviços ECS para Banco de Dados e Cache: Os servidores ECS interagem com o banco de dados primário,
      o réplica de leitura e o cache para armazenamento e recuperação de dados.
'''

# Importando a biblioteca e sub-bliotecas do Diagrams
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB, Route53

# Construindo a classe Diagram
with Diagram('Serviços Web em Clustered', show=True):
    dns = Route53('Serviço DNS')
    load_balancer = ELB('Balanceador de carga')

    with Cluster('Cluster de serviços ECS'):
        ecs_services = [ECS('Serviço Web 1'), ECS('Serviço Web 2'), ECS('Serviço Web 3')]
        
    with Cluster('Cluster de BDs'):
        db_primary = RDS("BD Primário")
        db_read_replica = RDS("Read Replica DB")

    cache = ElastiCache("Memcached")

    # Criando as conexões do Diagrama
    dns >> load_balancer >> ecs_services
    ecs_services >> db_primary
    ecs_services >> db_read_replica
    ecs_services >> cache

# EOC
