from import_Pauli_basis import *
    

def NOT_gate():
    '''
    Returns Pauli trasfer matrix of NOT gate
    '''
    return to_Pauli_T_matrix(np.array([[0, 1],
                                       [1, 0]]))



def Ry_gate(theta): # transfer matrix in Pauli basis
    return Qobj(np.array([[1, 0, 0, 0],
                          [0, np.cos(theta), 0, np.sin(theta)],
                          [0, 0, 1, 0],
                          [0, -np.sin(theta), 0, np.cos(theta)]]))




def Hadamard_gate():
    '''
    Returns Pauli trasfer matrix of Hadamard gate
    '''
    return to_Pauli_T_matrix(1/np.sqrt(2)*np.array([[1, 1],
                                       [1, -1]]))