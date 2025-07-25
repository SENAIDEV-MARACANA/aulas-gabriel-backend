--Primeiro cadastro, depois marcação

--Cadastro do paciente
INSERT INTO paciente (nome, telefone)
VALUES ('Roberto Dias', '(21)91212-3434')

--Cadastro médico se não estiver no sistema
INSERT INTO medico (nome, especializacao)
VALUES ('Marcos Almeida', 'Clínico Geral')

--Consulta de id 
SELECT id FROM paciente WHERE nome = 'Roberto Dias';
SELECT id FROM medico WHERE nome = 'Marcos Almeida';

--agendamento
INSERT INTO consulta (paciente_id, medico_id, data, hora)
VALUES (4, 5, '2024-07-15', '14:30');