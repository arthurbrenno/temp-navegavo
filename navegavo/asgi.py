"""
NavegAVÔ - Assistente Digital para Idosos

Copyright (C) 2024 Arthur Brenno Ribeiro Coelho

Este programa é software livre: você pode redistribuí-lo e/ou modificá-lo
sob os termos da GNU Affero General Public License conforme publicada pela
Free Software Foundation, seja a versão 3 da Licença, ou
(a seu critério) qualquer versão posterior.

Este programa é distribuído na esperança de que seja útil,
mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
COMERCIABILIDADE ou ADEQUAÇÃO A UM DETERMINADO FIM. Veja a
GNU Affero General Public License para mais detalhes.

Você deve ter recebido uma cópia da GNU Affero General Public License
junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

Desenvolvido por: Arthur Brenno Ribeiro Coelho
                  Universidade de Uberaba - UNIUBE
                  Curso de Sistemas de Informação

Data de criação: 11 de setembro de 2024

Descrição:
O NavegAVÔ é um assistente digital projetado para facilitar o uso de
tecnologia por idosos, promovendo inclusão digital e segurança online.
O aplicativo oferece uma variedade de funcionalidades adaptadas às
necessidades específicas deste público.

Funcionalidades Principais:
1. Assistência à Navegação: Tutorial interativo e interface simplificada.
2. Segurança Digital: Detector de fraudes e alertas de segurança.
3. Comunicação: Videochamadas e mensagens simplificadas.
4. Saúde e Bem-estar: Lembretes de medicação e monitoramento de saúde.
5. Aprendizagem e Entretenimento: Cursos online e biblioteca digital adaptada.
6. Acessibilidade: Ajustes de fonte, temas de alto contraste e leitor de tela.
7. Suporte e Assistência: Chat de suporte e guias passo a passo.
8. Personalização: Perfil de usuário adaptável e modo familiar.

NOTA SOBRE A ARQUITETURA:
Este projeto foi desenvolvido como parte de um trabalho acadêmico com
restrições de tempo significativas. Consequentemente, a implementação atual
não segue estritamente os princípios de Domain-Driven Design (DDD) e
Clean Architecture. Reconheço que uma aplicação mais robusta desses
conceitos arquiteturais melhoraria a estrutura e a manutenibilidade do código.
Futuras iterações do projeto devem considerar uma refatoração para alinhar
melhor a implementação com esses princípios de design de software.
Observe que a injeção de dependência também não está muito bem organizada.
Isso se deve à falta de tempo para implementar uma solução mais elegante
devido a sobrecarga de trabalho da Universidade e prazos apertados.

Para mais informações ou permissões, entre em contato com:
arthur.brenno@uniube.br

Versão: 1.0.0
"""

from .features.screen_chat.controllers import ScreenChatController  # type: ignore
from litestar import Litestar

app = Litestar(route_handlers=[ScreenChatController], path="/api")
