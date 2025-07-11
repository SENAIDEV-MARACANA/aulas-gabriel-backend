--Consulta A 
SELECT paciente.nome, consulta.hora
FROM consulta
INNER JOIN paciente ON consulta.paciente_id = paciente.id 
INNER JOIN medico ON consulta.medico_id = medico.id 
WHERE consulta.data = '2024-05-21'
    AND medico.nome = 'Carlos Andrade'

--Consulta B 
SELECT medico.especializacao, consulta.hora, medico.nome
FROM consulta
INNER JOIN paciente ON consulta.paciente_id = paciente.id
INNER JOIN medico ON consulta.medico_id = medico.id
WHERE consulta.data = '2024-05-21'
    AND paciente.nome = 'Beatriz Ribeiro'