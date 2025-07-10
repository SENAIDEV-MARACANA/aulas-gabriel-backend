--cancelamento consulta

DELETE FROM consulta
WHERE id = 15;

-- correção de dado de telefone errado

UPDATE paciente
SET telefone = '(21) 99999-8888'
WHERE if = 1001;

