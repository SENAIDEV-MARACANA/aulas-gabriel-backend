--cancelamento consulta

DELETE FROM consulta
WHERE id = 15;

-- correção de dado de telefone errado

UPDATE paciente
SET telefone = '(21) 99999-8888'
WHERE id = 1001;

-- o paciente quer apagar os dados na clinica só que tem consulta registrada

-- quando tentamos deletar direto da tabela paciente da erro, pois tem consultas ligadas a ele na tabela consultas.

-- Ordem correta de deleção dos dados : 1º apaga todas as consultas relaionadas ao paciente

DELETE FROM consulta
WHERE paciente_id = 1001;

--depois, apaga o dado do paciente 

DELETE FROM paciente
WHERE id = 1001;




